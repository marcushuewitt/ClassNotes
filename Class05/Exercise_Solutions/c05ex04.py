"""
Author:         Tim Smith
Description:    Solution to Class04 Ex5
"""

import string
import random

# create a list structure containing all the letters
letters = list(string.ascii_letters)
# sample without replacement (use random sample from the random library to shuffle letters)
codes = random.sample(letters, k=len(letters))

# create an encrypt and decrypt dictionary
encrypt = dict(zip(letters, codes))
decrypt = dict(zip(codes, letters))

plain_text = input("Please enter the phrase you would like to encrypt: \n")

cipher_text = ""
for ch in plain_text:
    if ch in string.ascii_letters:
        cipher_text += encrypt[ch]
    else:
        cipher_text += ch

print("Your encrypted text is...")
print(cipher_text)

# this wasn't part of the exercises, but for those looking to learn more python techniques, this is a good example
# of how you can use a for loop to traverse a dictionaries key value pairs - and sort a dictionary by key values
ans = input("Would you like the decode key? [Y/N]")
if ans == "Y" or ans == "y":
    print("Here is your decode table: ")
    for code, letter in sorted(decrypt.items()): # pull key value pairs from a sorted dictionary
        print(code + " -> ", letter)
