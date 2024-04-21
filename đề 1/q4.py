# merge first name and last name as single token in sentence
#input: textt =" Robert Langdon is a famous character in Ho Ton Bao various novels."
#output: "Robert Langdon", "is","a", "famous", character","Ho Ton",  "in", "various", "novels"

def merge_name(text):
    text = text.split()
    for i in range(len(text)-1):
        if text[i].istitle() and text[i+1].istitle():
            text[i] = text[i] + " " + text[i+1]
            text.pop(i+1)
    return text

text = "Robert Langdon is a famous character in various novels."
tokens = merge_name(text)
for token in tokens:
    print(token)