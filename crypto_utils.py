from cryptography.fernet import Fernet, InvalidToken

def generate_key():
    """Generates a new encryption key and saves it to key.key"""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """Loads the encryption key from key.key"""
    with open("key.key", "rb") as key_file:
        return key_file.read()

def encrypt_message(message: str) -> bytes:
    """Encrypts a plain text message and returns ciphertext bytes"""
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(message.encode("utf-8"))

def decrypt_message(token: bytes) -> str:
    """Decrypts ciphertext bytes back into plain text.
    Returns an error message string if decryption fails."""
    try:
        key = load_key()
        fernet = Fernet(key)
        return fernet.decrypt(token).decode("utf-8")
    except InvalidToken:
        return "❌ Error: Invalid key or corrupted message. Cannot decrypt."
    except FileNotFoundError:
        return "❌ Error: Encryption key file not found."