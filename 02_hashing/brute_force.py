import hashlib
import random
import string

# alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
alphabet = string.printable
length = 3


def generate(alphabet, max_len):
    if max_len <= 0:
        return
    for c in alphabet:
        yield c
    for c in alphabet:
        for next in generate(alphabet, max_len-1):
            yield c + next


text = ""
for i in range(length):
    text += alphabet[random.randint(0, len(alphabet)-1)]
print(text)
md5hash = hashlib.sha256(text.encode()).hexdigest()
print(md5hash)
print("==========================")

for x in generate(alphabet, length):
    testHash = hashlib.sha256(x.encode()).hexdigest()
    if testHash == md5hash:
        print("Found: " + x)
        print(testHash)
        break
