from Crypto.Cipher import AES
import base64

def encrypt_data(data, key="secretkey1234567"):
    cipher = AES.new(key.encode("utf-8"), AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode("utf-8"))
    return base64.b64encode(ciphertext).decode("utf-8")
