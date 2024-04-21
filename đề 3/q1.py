#define a function percent(word,text) that calculates how often a give word occurs in a text and express the result as as percentage

import re

def percent(word, text):
    pattern = r"\b\w+\b"
    token = re.findall(pattern, text)
    total_words = len(token)
    word_count = token.count(word)
    return (word_count/total_words)*100

text = "John lives in Canada. James lives in America, though he's not from there lives lives lives lives lives lives"
word = "lives"
print(f"The word '{word}' occurs in the text  {percent(word, text)}% of the time")
    
