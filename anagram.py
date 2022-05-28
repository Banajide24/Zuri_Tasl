def freq(word):
    freq_dict = {}
    for char in word:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict
# initialize a list
anagram_list = []
for word_1 in word_list: 
    for word_2 in word_list: 
        if word_1 != word_2 and (freq(word_1) == freq(word_2)):
            anagram_list.append(word_1)
print(anagram_list)
