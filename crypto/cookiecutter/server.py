from flask import Flask, request, render_template, redirect, make_response
from Crypto import Random
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class ECBOracle:
    def __init__(self):
        self.key = Random.new().read(AES.block_size)

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_ECB)
        return b64encode(cipher.encrypt(pad(data, AES.block_size))).decode()
    
    def decrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_ECB)
        ciphertext = b64decode(data)
        return unpad(cipher.decrypt(ciphertext), AES.block_size)
    
class Profile:
    email = None
    last_uid = 0
    uid = None
    role = 'user'

    def __init__(self, email : str, uid=None, role=None):
        Profile.last_uid += 1
        if uid:
            self.uid = uid
        else:
            self.uid = Profile.last_uid
        if role:
            self.role = role
        else:
            self.role = 'user'
        self.email = email.replace('&','').replace('=','')

    def __str__(self):
        return f"email={self.email}&uid={self.uid}&role={self.role}"
    
def kvparse(input : str):
    finobj = {}
    key = True
    tempkey = ''
    tempval = ''
    for i in input:
        if i == '&':
            finobj[tempkey] = tempval
            tempkey = ''
            tempval = ''
            key = True
        elif i == '=':
            key = False
        elif key:
            tempkey += i
        else:
            tempval += i
    finobj[tempkey] = tempval
    return finobj

def profile_for(input : str):
    return Profile(input)

def get_user_input(inp : str, oracle : ECBOracle):
    prof = profile_for(inp)
    userinfo = oracle.encrypt(str(prof).encode())
    return userinfo

def decrypt_user_input(inp : bytes, oracle : ECBOracle):
    return Profile(**kvparse(oracle.decrypt(inp).decode()))

###########################################################################
############### The Flask Web Server part #################################
###########################################################################

app = Flask(__name__)

oracle = ECBOracle()

@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@app.route("/login", methods=['POST'])
def register():
    user_email = request.form['email']
    cookie = get_user_input(user_email, oracle)
    response = make_response(render_template('home.html'))
    response.set_cookie('cookie', cookie)
    return response

@app.route("/authenticate", methods=['GET'])
def auth():
    cookie = request.cookies.get('cookie')
    user_info = decrypt_user_input(cookie.encode(), oracle)
    print(user_info)
    if user_info.role == 'admin':
        response = make_response(render_template('flag.html'))
        response.set_cookie('cookie', cookie) 
        return response
    else:
        response = make_response(render_template('failed_home.html'))
        response.set_cookie('cookie', cookie)
        print("failed auth")
        return response

@app.errorhandler(Exception)
def handle_error(error):
    print(f"Error: {error}")
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=1337, threaded=True)