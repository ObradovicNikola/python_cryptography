from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# key can be 256 bits long
key = os.urandom(32)

# iv must be 16 bytes (128 bits) long
iv = os.urandom(16)

aesCipher = Cipher(algorithms.AES(key),
                   modes.CBC(iv),
                   backend=default_backend())
aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

plain = b"0123456789ABCDEF"
cipher = aesEncryptor.update(plain)
recover = aesDecryptor.update(cipher)
if plain == recover:
    print("[PASS]")
else:
    print("plain", plain)
    print("cipher", cipher.hex())
    print("recover", recover)
    print("[FAIL]")
