with open("justterrible.txt", "rb") as f:
    bytestream = f.read()

bytestream = bytestream.lstrip(b"hello, there").rstrip(b"general kenobi")

flag = ""
j = 0
for i in bytestream:
    if i == 1:
        flag += chr(j)
        j = 0
    else:
        j += 1

print(flag)