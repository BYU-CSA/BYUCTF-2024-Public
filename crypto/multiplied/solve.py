from Crypto.Util.Padding import unpad
import hashlib
from Crypto.Cipher import AES
from base64 import b64decode
from ellipticcurve import *

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv, ciphertext):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = b64decode(ciphertext)
    iv = b64decode(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')
    
def main():
    ciphertext = b'SllGMo5gxalFG9g8j4KO0cIbXeub0CM2VAWzXo3nbIxMqy1Hl4f+dGwhM9sm793NikYA0EjxvFyRMcU2tKj54Q=='
    iv = b'MWkMvRmhFy2vAO9Be9Depw=='

    curve = EllipticCurve(13, 245, 335135809459196851603485825030548860907)
    start_point = CurvePoint(14592775108451646097, 237729200841118959448447480561827799984, curve)

    final_point = start_point * 1337
    plaintext = decrypt_flag(final_point.x, iv, ciphertext)
    print(plaintext)

if __name__ == "__main__":
    main()
