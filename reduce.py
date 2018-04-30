from functools import reduce

with open("doriangray.txt", 'r') as f:
    story = f.read()

BOOK = story.split()

BOOK = [x.strip(".,!:;?\"'()[]/-").lower() for x in BOOK]

# Return frequency of string word 
def word_freq(word):
    return len([i for i in BOOK if i == word.lower()])

# Return total frequency of list words
def words_freq(words):
    return reduce((lambda x,y: x + y), [word_freq(i) for i in words])  

# Return most frequent word
def top_word():
    pass

#print story
print word_freq("Dorian")
print word_freq("Gray")
print words_freq(["Dorian","Gray"])
