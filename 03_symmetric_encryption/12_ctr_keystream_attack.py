# ACME generates a purchase message in their storefront.
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# WARNING! Never do this. Reusing a key/IV is irresponsible!
preshared_key = os.urandom(16)
preshared_iv = os.urandom(16)


aesContext = Cipher(algorithms.AES(preshared_key),
                    modes.CTR(preshared_iv),
                    backend=default_backend())
encryptor = aesContext.encryptor()
decryptor = aesContext.decryptor()

purchase_message1 = b"""
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

encrypted_message1 = encryptor.update(purchase_message1)
print(encryptor.finalize())
print("msg1: ", encrypted_message1.hex())
print(len(encrypted_message1))

purchase_message2 = b"""
<XML>
  <CreditCardPurchase>
    <Merchant>Acme Inc</Merchant>
    <Buyer>Boby Moris</Buyer>
    <Date>12/21/2001</Date>
    <Amount>$100.00</Amount>
    <CCNumber>555-555-555-009</CCNumber
  </CreditCardPurchase>
</XML>
"""

# reusing the same key/iv is bad
encryptor = aesContext.encryptor()
encrypted_message2 = encryptor.update(purchase_message2)
print("msg2: ", encrypted_message2.hex())
print(len(encrypted_message2))

# purchase_message1 is known attackers message
# encrypted messages are intercepted and known
keystream = bytes([a ^ b for a, b in zip(
    purchase_message1, encrypted_message1)])
print("keystream: ", keystream.hex())
print(len(keystream))


decrypted_message2 = bytes(
    [a ^ b for a, b in zip(encrypted_message2, keystream)])

print("decrypted_message2: ", decrypted_message2.decode())
if(decrypted_message2 == purchase_message2):
    print("Success!")
else:
    print("Failed!")
