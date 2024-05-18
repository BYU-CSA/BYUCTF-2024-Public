import socket
import struct
# import antigravity

class MCQuery:
    id = 0
    retries = 0
    max_retries = 3
    timeout = 10
    
    def __init__(self, host, port, **kargs):
        self.addr = (host, port)
        if 'max_retries' in kargs:
            self.max_retries = kargs['max_retries']
        if 'timeout' in kargs:
            self.timeout = kargs['timeout']
       
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(self.timeout)
        self.handshake()
    
    def write_packet(self, type, payload):
        o = b'\xFE\xFD' + struct.pack('>B', type) + struct.pack('>l', self.id) + payload
        # thing = f"0{type}"
        # o = b'\xFE\xFD' + bytes(type) + struct.pack('>l', self.id) + payload
        self.socket.sendto(o, self.addr)
    
    def read_packet(self):
        buff = self.socket.recvfrom(2048)[0]
        type = struct.unpack('>B', buff[0:1])[0]
        id   = struct.unpack('>l', buff[1:5])[0]
        return type, id, buff[5:]
    
    def handshake(self):
        self.id += 1
        self.write_packet(9, b'')
        try:
            type, id, buff = self.read_packet()
        except:
            self.retries += 1
            if self.retries == self.max_retries:
                raise Exception('Retry limit reached - server down?')
            return self.handshake()
        
        self.retries = 0
        self.challenge = struct.pack('>l', int(buff[:-1]))
    
    def basic_stat(self):
        self.write_packet(0, self.challenge)
        try:
            type, id, buff = self.read_packet()
        except:
            self.handshake()
            return self.basic_stat()
        
        data = {}
        
        #I don't seem to be receiving this field...
        #data['ip'] = socket.inet_ntoa(buff[:4])[0]
        #buff = buff[4:]
        
        #Grab the first 5 string fields
        data['motd'], data['gametype'], data['map'], data['numplayers'], data['maxplayers'], buff = buff.split(b'\x00', 5)
        # data['motd'], data['gametype'], data['map'], data['numplayers'], data['maxplayers'], buff = buff.split()
        
        #Unpack a big-endian short for the port
        data['hostport'] = struct.unpack('<h', buff[:2])[0]
        
        #Grab final string component: host name
        data['hostname'] = buff[2:-1]
        
        #Encode integer fields
        for k in ('numplayers', 'maxplayers'):
            data[k] = int(data[k])

        return data
    
    def full_stat(self):
        #Pad request to 8 bytes
        self.write_packet(0, self.challenge + b'\x00\x00\x00\x00')
        try:
            type, id, buff = self.read_packet()
        except:
            self.handshake()
            return self.full_stat()    
        
        #Chop off useless stuff at beginning
        buff = buff[11:]
        
        #Split around notch's silly token
        items, players = buff.split(b'\x00\x00\x01player_\x00\x00')
        
        #Notch wrote "hostname" where he meant to write "motd"
        items = b'motd' + items[8:] 
        
        #Encode (k1, v1, k2, v2 ..) into a dict
        items = items.split(b'\x00')
        data = dict(zip(items[::2], items[1::2])) 

        #Remove final two null bytes
        players = players[:-2]
        
        #Split player list
        if players: data['players'] = players.split('\x00')
        else:       data['players'] = []
        
        #Encode ints
        for k in (b'numplayers', b'maxplayers', b'hostport'):
            data[k] = int(data[k])
        
        #Parse 'plugins'
        s = data[b'plugins']
        s = s.split(b': ', 1)
        data[b'server_mod'] = s[0]
        if len(s) == 1:
            data[b'plugins'] = []
        elif len(s) == 2:
            data[b'plugins'] = s[1].split(b'; ')

        return data

if __name__ == "__main__":
    # thing = MCQuery("127.0.0.1", 1361)
    thing = MCQuery("gaming.chal.cyberjousting.com", 1361)
    test = thing.basic_stat()
    print(test["motd"])
    test = thing.full_stat()
    print(test[b"motd"])
