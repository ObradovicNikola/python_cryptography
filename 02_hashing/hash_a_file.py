import hashlib

data = open("file.txt", "rb").read()

md5hash = hashlib.md5(data).hexdigest()

print(md5hash)
