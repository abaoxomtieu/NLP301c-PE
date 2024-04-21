from nltk.corpus import brown, nps_chat
from nltk.probability import FreqDist
import re
def get_data(document):
    match = [word for word in document if word.isalpha() and len(word) == 4]
    match = FreqDist(match).most_common()
    return match
document = nps_chat.words()
result = get_data(document)
for word, count in result:
    print(word + ":" + str(count))