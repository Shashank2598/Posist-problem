import base64
from Crypto.Cipher import AES

def encryption():
    msg_text = 'test some plain text here'.rjust(32)
    secret_key = '1234567890123456'

    cipher = AES.new(secret_key, AES.MODE_ECB)
    encoded = base64.b64encode(cipher.encrypt(msg_text))
    return encoded


def decryption(encoded):
    decoded = Crypto.Cipher.decrypt(base64.b64decode(encoded))
    return decoded.strip()
