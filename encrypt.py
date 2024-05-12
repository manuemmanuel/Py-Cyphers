import base64
from itertools import cycle

def xor_string(data, key):
    return ''.join([chr((ord(d) ^ ord(k)) & 0xFF) for d, k in zip(data, cycle(key))])

def encrypt_text(plain_text, key):
    encrypted_data = xor_string(plain_text, key)
    base64_bytes = base64.b64encode(encrypted_data.encode())
    base64_str = base64_bytes.decode('ascii')
    return base64_str

if __name__ == "__main__":
    message = "Welcome to my world!"
    
    key = "mysecretkey"
    cipher_text = encrypt_text(message, key)
    print(f"Encrypted Message: {cipher_text}")
