import hashlib
import random
import sys

block = "this is a list of transactions"
counter = 0

maxHash = 2 ** 238

blockstr = str(counter) + block
blockHash = int(hashlib.sha256((blockstr).encode()).hexdigest(), 16)
while (blockHash > maxHash):
    counter = random.randint(0, sys.maxsize)
    blockstr = str(counter) + block
    blockHash = int(hashlib.sha256((blockstr).encode()).hexdigest(), 16)

print("Mined the block!")
print(counter)
print(blockHash)
