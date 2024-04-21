from nltk.corpus import brown
from nltk.probability import FreqDist
words = brown.words()
freqDist = FreqDist(words)
for word, count in freqDist.items():
    if(count >= 3):
        print(word + ":" + str(count))
