# Hamming Distance
# Indicator of how different two strings are
# "...number of positions at which the corresponding symbols are different."
# Should be simple

string1 = input("Enter String 1 - ")
string2 = input("Enter String 2 - ")

len1 = len(string1)
len2 = len(string2)
counter = 0
if len1 == len2:
    for i in range(len1):
        if string1[i] != string2[i]:
            counter += 1
else:
    print("Not true hamming distance")
    smaller = len1 if len1 < len2 else len2
    larger = len1 if len1 > len2 else len2
    print(larger, smaller)
    for i in range(smaller):
        if string1[i] != string2[i]:
            counter += 1
    counter += (larger-smaller)
print("Hamming distance - ", counter)
