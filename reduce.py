from functools import reduce

with open("doriangray.txt", 'r') as f:
    story = f.read()

BOOK = story.split()

BOOK = [x.strip(".,!:;?\"'()[]/-").lower() for x in BOOK]

def word_freq(word):
    return len([x for x in BOOK if x == word.lower()])

def words_freq(words):
    return len([x for x in BOOK for y in words if x == y.lower()])

#print story
print word_freq("Dorian")
print word_freq("Gray")
print words_freq(["Dorian","Gray"])
