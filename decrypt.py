import base64
from itertools import cycle

def xor_string(data, key):
    return ''.join([chr((ord(d) ^ ord(k)) & 0xFF) for d, k in zip(data, cycle(key))])

def decrypt_text(cipher_text, key):
    base64_bytes = base64.b64decode(cipher_text)
    encrypted_data = base64_bytes.decode('ascii')
    decrypted_data = xor_string(encrypted_data, key)
    return decrypted_data
