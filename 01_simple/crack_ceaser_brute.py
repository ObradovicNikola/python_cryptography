import ceaser_cipher

ciphertext = "FANQADZAFFANQFTMFUEFTQCGQEFUAZ"

for(shift) in range(26):
    print(str(shift) + " " + ceaser_cipher.decrypt(ciphertext, shift))
