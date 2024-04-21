#write a function that takes a text and vocabulary as its arguments and returns the set of words that appear in the text but not in the vocabulary. both arguments can be represented as lists of strings.

import re
def tokenize(str):
    pattern = r"\b\w+\b"
    return re.findall(pattern, str)
def diff(text, vocab):
    return set([word for word in text if word not in vocab])

if __name__ == "__main__":
        
    vocab = " I am a student at FPT University"
    text = " I am a teacher at my home FPT"
    vocab = tokenize(vocab)
    text = tokenize(text)
    print(diff(text, vocab))