from encrypt import encrypt_text
from decrypt import decrypt_text

if __name__ == "__main__":
    message = "Welcome to my world!"
    key = "mysecretkey"
    cipher_text = encrypt_text(message, key)
    print(f"Encrypted Message: {cipher_text}")
    
    cipher_text = "X19fX2BgbG1lbm" 
    key = "mysecretkey"
    decrypted_message = decrypt_text(cipher_text, key)
    print(f"Decrypted Message: {decrypted_message}")
