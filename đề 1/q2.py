# find all the four-letter words in the Chat Corpus (text5). With the help of a frequency distribution (FreqDist), show these words in decreasing order of frequency.

import nltk
from nltk.corpus import webtext
from nltk.probability import FreqDist
words = webtext.words()

four_letter_words = [word for word in words if len(word) == 4]

fdist = FreqDist(four_letter_words)

print(fdist.most_common())

