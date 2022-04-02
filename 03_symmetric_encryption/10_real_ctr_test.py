from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class EncryptionManager:
    def __init__(self):
        key = b'YELLOW SUBMARINE'
        nonce = b'CHALENGECHALENGE'

        aes_context = Cipher(algorithms.AES(key),
                             modes.CTR(nonce),
                             backend=default_backend())
        self.encryptor = aes_context.encryptor()
        self.decryptor = aes_context.decryptor()

    def updateEncryptor(self, plaintext):
        return self.encryptor.update(plaintext)

    def finalizeEncryptor(self):
        return self.encryptor.finalize()

    def updateDecryptor(self, ciphertext):
        return self.decryptor.update(ciphertext)

    def finalizeDecryptor(self):
        return self.decryptor.finalize()


# Auto generate key/IV for encryption
manager = EncryptionManager()

plaintext = "This is a secret message. This is a secret message."

ciphertext = manager.updateEncryptor(plaintext.encode())
ciphertext += manager.finalizeEncryptor()

print(ciphertext.hex())

print(manager.updateDecryptor(ciphertext).decode())
print(manager.finalizeDecryptor().decode())
