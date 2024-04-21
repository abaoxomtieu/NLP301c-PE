import re
text = "Walter was feeling anxious. He was diagnosed today. he probably is the best person I know. "
pattern = r'\b\w+|[\.]'
matches = re.findall(pattern, text)
delimiters = ["is","the","was","."]
array = []
word_string = ""
for character in matches:
    if character not in delimiters:
        if word_string == "":
            word_string += character
        else:
            word_string += " " + character
        
    else:
        if word_string != "":
            array.append(word_string)
        word_string = ""
print(array)