# Generate bigrams for an input word
# "DUCK"
# ["DU","UC","CK"]


def generate_bigrams(word):
    word_len = len(word)
    bigrams = []
    for i in range(word_len-1):
        bg_temp = word[i]+word[i+1]
        bigrams.append(bg_temp)
    return bigrams
