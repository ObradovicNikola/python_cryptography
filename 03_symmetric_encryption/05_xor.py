import os

text = "CHALENGECHALENGE"
mask = os.urandom(16)

# xor the text with the mask
ciphertext = bytes([a ^ b for a, b in zip(text.encode(), mask)])

print(ciphertext.hex())

# decode the ciphertext
plaintext = bytes([a ^ b for a, b in zip(ciphertext, mask)])
print(plaintext.decode())
