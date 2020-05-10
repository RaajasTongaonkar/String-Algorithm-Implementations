# Dice's coeffecient
# Similarity between two strings
# n1 = set of bigrams in first string
# n2 = set of bigrams in second string
# Dice's coefficient = 2*|n1 AND n2|/ |n1|+|n2|

from generator import generate_bigrams
from common import common_bigrams
s1 = input("Enter a string - ")
s2 = input("Enter another string - ")
# print(s1, s2)

word1 = generate_bigrams(s1)
word2 = generate_bigrams(s2)
# print(word1, word2)

# Need to take the smaller list first to prevent counting of duplicates.
if len(word2) > len(word1):
    common_bg = common_bigrams(word1, word2)
else:
    common_bg = common_bigrams(word2, word1)
# print(len(common_bg))

dice_coeff = (2*len(common_bg))/(len(word1) + len(word2))
print("Dice's coefficient - ", dice_coeff)
