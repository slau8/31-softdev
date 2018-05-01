from functools import reduce

with open("doriangray.txt", 'r') as f:
    story = f.read()

BOOK = story.split()

BOOK = [x.strip(".,!:;?\"'()[]/-").lower() for x in BOOK]

TEST = ["word", "word", "word", "test", "the", "time", "time"]

# Return frequency of string word 
def word_freq(word, l):
    return reduce(lambda x, y: x + y, [1 for i in l if i == word.lower()])

# Return total frequency of list words
def words_freq(words, l):
    return reduce((lambda x,y: x + y), [word_freq(i, l) for i in words])

# Return most frequent word
def top_word(l):
    return reduce((lambda x, y: x if word_freq(x, l) > word_freq(y, l) else y), l)

#print story
print word_freq("Dorian", BOOK)
print word_freq("Gray", BOOK)
print words_freq(["Dorian","Gray"], BOOK)
print word_freq("word", TEST)
print word_freq("test", TEST)
print words_freq(["time","the"], TEST)
print top_word(TEST)
print top_word(BOOK)
