import ceaser_cipher

ciphertext = "FANQADZAFFANQFTMFUEFTQCGQEFUAZ"

shift = 0
word_count = 0

words = open("google-10000-english.txt", "r",
             errors="ignore").read().splitlines()

for k in range(26):
    plaintext = ceaser_cipher.decrypt(ciphertext, k)
    # plaintext to lowercase
    plaintext = plaintext.lower()
    curr_word_count = 0
    for word in words:
        if word in plaintext:
            curr_word_count += 1
    # print(k, ": ", curr_word_count)
    if(curr_word_count > word_count):
        shift = k
        word_count = curr_word_count


print("Shift:", shift)
print("Word count:", word_count)
print(ceaser_cipher.decrypt(ciphertext, shift))
