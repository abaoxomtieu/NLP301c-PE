import re
from nltk.corpus import stopwords, gutenberg
from nltk.probability import FreqDist

book_names = gutenberg.fileids()
selected_book = 'austen-emma.txt'
book_text = gutenberg.raw(selected_book)
# print(stopwords.words('english'))
def tokenize(text,top=50):
    pattern = r"\b\w+\b"
    token = re.findall(pattern, text)
    #split stopwords have in token list
    token = [word for word in token if word.lower() not in stopwords.words('english')]
    token = FreqDist(token).most_common(top)
    return token

# print(len(tokenize("book_text")))
result = tokenize(book_text)
for i in result:
    print(i[0] + ":" + str(i[1]))