from crypto_utils import generate_key, encrypt_message, decrypt_message

generate_key()  # Run once to create key.key

msg = "This is a test message"
encrypted = encrypt_message(msg)
print("Encrypted:", encrypted)

decrypted = decrypt_message(encrypted)
print("Decrypted:", decrypted)

# Test with corrupted data
fake_data = b"not_a_real_token"
print("Corrupted test:", decrypt_message(fake_data))