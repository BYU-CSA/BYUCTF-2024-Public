flag = "byuctf{wh4ts_4_nu11_byt3_4nyw4ys}"

enc = b'hello, there'
for i in flag:
    enc += bytes(ord(i))
    enc += bytes([1])
enc += b'general kenobi'

with open("justterrible.txt", "wb") as f:
    f.write(enc)