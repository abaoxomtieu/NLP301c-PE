import re
from nltk.tokenize import regexp_tokenize


def text_split(text: str) -> list:

    pattern_1 = r"\w+|[^\w\s]" ## ^ outside of [] is start, but in [] then negative
    pattern_2 = r"\w+|\." 
    list_word= re.findall(pattern_2,text) 

    return list_word

if __name__ == "__main__":


    #Create dataset;
    text = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."

    #Show answers;
    list_word = text_split(text)
    print(list_word)