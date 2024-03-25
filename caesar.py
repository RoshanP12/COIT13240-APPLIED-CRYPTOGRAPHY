# Caesar cipher
import englishcipher

# Caesar encrypt: input key and plaintext; output ciphertext
def encrypt(key, plaintext):
	# Convert plaintext text to numerical values in list
	plaintext_list = englishcipher.text_to_nums(plaintext)


	# initialise ciphertext list
	ciphertext_list = []

	# for each letter in the list, add key and mod 26
	for p in plaintext_list:
		c = (p + key) % 26
		ciphertext_list.append(c)

	# convert ciphertext numerical values back to text
	ciphertext = englishcipher.nums_to_text(ciphertext_list)

	return ciphertext

# Test caesar encrypt
c = encrypt(9, "belgium")
print(c)
