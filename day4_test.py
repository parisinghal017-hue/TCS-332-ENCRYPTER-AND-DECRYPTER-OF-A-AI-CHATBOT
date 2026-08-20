from cryptography.fernet import Fernet

# Step 1: Generate a key
key = Fernet.generate_key()
print("Generated Key:", key)

# Step 2: Create a Fernet object using this key
fernet = Fernet(key)

# Step 3: Encrypt a message
message = "Hi, how are you?"
encrypted_message = fernet.encrypt(message.encode("utf-8"))
print("\nEncrypted Message:", encrypted_message)

# Step 4: Decrypt the message back
decrypted_message = fernet.decrypt(encrypted_message).decode("utf-8")
print("\nDecrypted Message:", decrypted_message)

# Step 5: Encrypt the SAME message again — see it looks different
encrypted_message_2 = fernet.encrypt(message.encode("utf-8"))
print("\nSame message encrypted again:", encrypted_message_2)
print("Is it same as before?", encrypted_message == encrypted_message_2)
# Experiment: Try decrypting with a WRONG key
wrong_key = Fernet.generate_key()
wrong_fernet = Fernet(wrong_key)

try:
    wrong_fernet.decrypt(encrypted_message)
except Exception as e:
    print("\nError occurred! Type of error:", type(e).__name__)