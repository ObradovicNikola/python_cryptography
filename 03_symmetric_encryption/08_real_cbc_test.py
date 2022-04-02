from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = b'YELLOW SUBMARINE'
iv = b'CHALENGECHALENGE'

aesCipher = Cipher(algorithms.AES(key),
                   modes.CBC(iv),
                   backend=default_backend())
aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()


plaintext = "This is a secret message."
plaintext += '\x00' * (16 - len(plaintext) % 16)
# plaintext += 'e' * (16 - len(plaintext) % 16)

ciphertext = aesEncryptor.update(plaintext.encode()).hex()
print(ciphertext)

# decrypt
print(aesDecryptor.update(bytes.fromhex(ciphertext)).decode())
