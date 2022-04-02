def encrypt(plaintext, shifts):
    shifted = ""
    for c in plaintext:
        if c.isalpha():
            if c.isupper():
                shifted += chr((ord(c) + shifts - ord('A')) % 26 + 65)
            else:
                shifted += chr((ord(c) + shifts - 'a') % 26 + 97)
        else:
            shifted += c
    return shifted


def decrypt(ciphertext, shifts):
    shifted = ""
    for c in ciphertext:
        if c.isalpha():
            if c.isupper():
                shifted += chr((ord(c) - shifts - ord('A')) % 26 + 65)
            else:
                shifted += chr((ord(c) - shifts - 'a') % 26 + 97)
        else:
            shifted += c
    return shifted


# shifts = 2

# plaintext = "HELLO WORLD"

# encrypted = encrypt(plaintext, shifts)
# print(encrypted)
# print(decrypt(encrypted, shifts))
