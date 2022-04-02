# implement AES CTR mode using AES ECB

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = b'YELLOW SUBMARINE'
iv = b'CHALENGECHALENGE'

# ecb cipher
aesCipher = Cipher(algorithms.AES(key),
                   modes.ECB(),
                   backend=default_backend())
aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()


plaintext = "This is a secret message. This is a secret message."


def encrypt(plaintext):
    nounce = iv
    keystream = b''
    while (len(keystream) < len(plaintext)):
        keystream += aesEncryptor.update(nounce)
        nounce = hex(int(nounce.hex(), 16) + 1)[2:]
        nounce = bytes.fromhex(nounce)

    # xor plaintext with keystream
    ciphertext = bytes([a ^ b for a, b in zip(plaintext.encode(), keystream)])
    return ciphertext.hex()


def decrypt(ciphertext):
    nounce = iv
    keystream = b''
    while (len(keystream) < len(ciphertext)):
        keystream += aesEncryptor.update(nounce)
        nounce = hex(int(nounce.hex(), 16) + 1)[2:]
        nounce = bytes.fromhex(nounce)

    # xor ciphertext with keystream
    plaintext = bytes([a ^ b for a, b in zip(ciphertext, keystream)])
    return plaintext.decode()


ciphertext = encrypt(plaintext)
print(ciphertext)
text = decrypt(bytes.fromhex(ciphertext))
print(text)
