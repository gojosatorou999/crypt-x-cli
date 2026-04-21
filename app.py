import argparse
import sys
from cryptography.fernet import Fernet

def generate_key():
    """Generates a key and saves it to a file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to 'secret.key'. Keep this file safe!")

def load_key():
    """Loads the key from the current directory named 'secret.key'."""
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("Error: 'secret.key' not found. Generate one first using 'gen-key'.")
        sys.exit(1)

def encrypt_text(text):
    """Encrypts text using the saved key."""
    key = load_key()
    f = Fernet(key)
    encrypted_text = f.encrypt(text.encode())
    return encrypted_text.decode()

def decrypt_text(encrypted_text):
    """Decrypts text using the saved key."""
    key = load_key()
    f = Fernet(key)
    try:
        decrypted_text = f.decrypt(encrypted_text.encode())
        return decrypted_text.decode()
    except Exception:
        print("Error: Decryption failed. Ensure the key is correct and the text hasn't been tampered with.")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="CryptX: A simple CLI tool for text encryption/decryption.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: gen-key
    subparsers.add_parser("gen-key", help="Generate a new encryption key")

    # Command: encrypt
    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt a text message")
    encrypt_parser.add_argument("text", help="The text to encrypt")

    # Command: decrypt
    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt an encrypted message")
    decrypt_parser.add_argument("token", help="The encrypted token to decrypt")

    args = parser.parse_args()

    if args.command == "gen-key":
        generate_key()
    elif args.command == "encrypt":
        result = encrypt_text(args.text)
        print(f"Encrypted message:\n{result}")
    elif args.command == "decrypt":
        result = decrypt_text(args.token)
        print(f"Decrypted message:\n{result}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
