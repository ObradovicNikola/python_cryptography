# implement AES CBC mode using AES ECB

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


plaintext = "This is a secret message."

ciphertext = b''


def encrypt(plaintext):
    plaintext_bytes = plaintext.encode()
    prev_block = iv
    ciphertext = b''
    while(len(plaintext_bytes) > 16):
        plain_block = plaintext_bytes[:16]
        plaintext_bytes = plaintext_bytes[16:]
        # xor plaintext with previous block
        cipher_block = bytes([a ^ b for a, b in zip(plain_block, prev_block)])

        encrypted_block = aesEncryptor.update(cipher_block)
        prev_block = encrypted_block
        ciphertext += encrypted_block
    if(len(plaintext_bytes) > 0):
        plaintext_bytes += b'\x00' * (16 - len(plaintext_bytes))
        cipher_block = bytes(
            [a ^ b for a, b in zip(plaintext_bytes, prev_block)])
        ciphertext += aesEncryptor.update(cipher_block)
    print(ciphertext.hex())
    return ciphertext.hex()


def decrypt(ciphertext):
    prev_block = iv
    plaintext = b''
    while(len(ciphertext) > 0):
        cipher_block = ciphertext[:16]
        ciphertext = ciphertext[16:]
        plain_block = aesDecryptor.update(cipher_block)
        plain_block = bytes([a ^ b for a, b in zip(plain_block, prev_block)])
        prev_block = cipher_block
        plaintext += plain_block
    print(plaintext.decode())
    return plaintext.decode()


ciphertext = encrypt(plaintext)
decrypt(bytes.fromhex(ciphertext))
