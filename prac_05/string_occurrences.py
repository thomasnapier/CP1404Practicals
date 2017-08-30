word_occurrences = {}
string = input("Text: ")
words = string.split()
for word in words:
    frequency = word_occurrences.get(word, 0)
    if frequency == 0:
        word_occurrences[word] = 1
    else:
        word_occurrences[word] = frequency + 1
words = list(word_occurrences.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_occurrences[word]))