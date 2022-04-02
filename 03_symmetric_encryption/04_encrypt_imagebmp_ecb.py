import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(16)
iv = os.urandom(16)

aesCipher = Cipher(algorithms.AES(key),
                   modes.ECB(),
                   backend=default_backend())
# aesCipher = Cipher(algorithms.AES(key),
#                    modes.CBC(iv),
#                    backend=default_backend())
aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()


ifile, ofile = sys.argv[1:3]
print(ifile)
print(ofile)
with open(ifile, "rb") as reader:
    with open(ofile, "wb+") as writer:
        image_data = reader.read()
        # find header length with a hex editor
        header, body = image_data[:139], image_data[139:]
        body += b"\x00"*(16-(len(body) % 16))
        writer.write(header + aesEncryptor.update(body))
