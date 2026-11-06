import random
import string

# Generate unique characters
chars = list(string.printable)

# Generate encryption key
keys = chars.copy()
random.SystemRandom().shuffle(keys)

# Create encryption and decryption mappings
encryption_map = dict(zip(chars, keys))
decryption_map = {v: k for k, v in encryption_map.items()}


def encrypt(message):
    encrypted_text = ""

    for char in message:
        encrypted_text += encryption_map.get(char, char)

    return encrypted_text


def decrypt(message):
    decrypted_text = ""

    for char in message:
        decrypted_text += decryption_map.get(char, char)

    return decrypted_text


# Main program
original_text = input("Enter text to encrypt: ")

encrypted_text = encrypt(original_text)
decrypted_text = decrypt(encrypted_text)

print("\nOriginal:", original_text)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
