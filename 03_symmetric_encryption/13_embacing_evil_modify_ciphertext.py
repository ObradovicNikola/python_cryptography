# You work for (or own!) Evil LLC. Time to steal some payments from Acme. Start with one of the
# encrypted payment messages you created in the earlier exercises. Calculate the size of the
# header up through the identification of the merchant and extract that many bytes of the
# encrypted data. XOR the plaintext header with the ciphertext header to get the keystream. Once
# you have this, XOR the extracted keystream with a header identifying Evil LLC as the merchant.
# This is the “evil” ciphertext. Copy it over the bytes of the encrypted file to create a new payment
# message identifying your company as the recipient. Prove that it works by decrypting the
# modified file.
# The key lesson here is that encryption is insufficient to protect data by itself. In subsequent
# chapters, we will use message authentication codes, authenticated encryption, and digital
# signatures to ensure that data cannot be altered without disrupting communications.


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(16)
iv = os.urandom(16)


aesContext = Cipher(algorithms.AES(key),
                    modes.CTR(iv),
                    backend=default_backend())
encryptor = aesContext.encryptor()
decryptor = aesContext.decryptor()

purchase_message = b"""
<XML>
  <CreditCardPurchase>
    <Merchant>Acme Inc</Merchant>
    <Buyer>John Smith</Buyer>
    <Date>01/01/2001</Date>
    <Amount>$100.00</Amount>
    <CCNumber>555-555-555-006</CCNumber
  </CreditCardPurchase>
</XML>
"""

encrypted_message = encryptor.update(purchase_message)
print("msg: ", encrypted_message.hex())

purchase_message_known_header = b"""
<XML>
  <CreditCardPurchase>
    <Merchant>Acme Inc</Merchant>
"""

keystream = bytes([a ^ b for a, b in zip(
    encrypted_message, purchase_message_known_header)])
# print("keystream: ", keystream.hex())

evil_header = b"""
<XML>
  <CreditCardPurchase>
    <Merchant>Evil LLC</Merchant>
"""

encrypted_evil_header = bytes([a ^ b for a, b in zip(evil_header, keystream)])
evil_encrypted_message = encrypted_evil_header + \
    encrypted_message[len(encrypted_evil_header):]
print("msg: ", evil_encrypted_message.hex())

evil_decrypted_message = decryptor.update(evil_encrypted_message)


print("\nRecovered:\n" + evil_decrypted_message.decode() + "\n")
