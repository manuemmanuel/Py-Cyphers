from encrypt import encrypt_text
from decrypt import decrypt_text

def menu():
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Exit")

def encrypt_menu():
    message = input("Enter the text to encrypt: ")
    key = input("Enter the encryption key: ")
    cipher_text = encrypt_text(message, key)
    print(f"Encrypted Message: {cipher_text}")

def decrypt_menu():
    cipher_text = input("Enter the text to decrypt: ")
    key = input("Enter the decryption key: ")
    decrypted_message = decrypt_text(cipher_text, key)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            encrypt_menu()
        elif choice == '2':
            decrypt_menu()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
