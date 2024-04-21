import re
from nltk.probability import FreqDist
def shorten(text, n):
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text)
    # Count the frequency of each word
    word_counts = FreqDist(words)

    # Identify the n most frequent words
    most_common_words = [word for word, _ in word_counts.most_common(n)]
    # Remove the most frequent words from the text
    shortened_text = ' '.join(word for word in words if word not in most_common_words)

    return shortened_text  # Capitalize the first letter of the shortened text

text = """Write a function shorten(text,n) to process a text, omitting the n most frequently occurring words of the text. How readable is it?"""
n = 4
shortened_text = shorten(text, 4)
print(shortened_text)
