import random
import string

# Create a clean, unique list of characters (no duplicates)
# string.printable includes letters, digits, punctuation, and whitespace
chars = list(set(string.printable))

# Create the key mapping
keys = chars.copy()
random.shuffle(keys)

# Build a mapping dictionary for instant lookups
encryption_map = dict(zip(chars, keys))

# Encryption process
original_text = input("Enter the text to be encrypted: ")
new_text = ""

for char in original_text:
    # If the character is in our list, swap it. If not, leave it as is.
    new_text += encryption_map.get(char, char)

print("\nOriginal text:", original_text)
print("Encrypted text:", new_text)
