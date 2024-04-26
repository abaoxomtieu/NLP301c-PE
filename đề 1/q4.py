# merge first name and last name as single token in sentence
#input: textt =" Robert Langdon is a famous character in Ho Ton Bao various novels."
#output: "Robert Langdon", "is","a", "famous", character","Ho Ton",  "in", "various", "novels"
import re
def merge_name(text):
    text = text.split()
    for i in range(len(text)-1):
        if text[i].istitle() and text[i+1].istitle():
            text[i] = text[i] + " " + text[i+1]
            text.pop(i+1)
    return text

def tokenize(text):
    text = text.split()
    one_token = ""
    array = []
    for token in text:
        if token.istitle():
            if one_token =="":
                one_token += token

            else:
                one_token += " " + token
        else:
            if(one_token!=""):
                array.append(one_token)
            one_token = ""
            array.append(token)
    return array

text = "Robert Langdon is a famous character Abao Xom Tieu in various novels."


token = tokenize(text)
print("token: ", token)