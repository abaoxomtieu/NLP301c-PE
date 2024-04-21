import re
# text = "I like arithmetic 3 7 5+4 like addition, subtraction example is 4+3 or 6+7*5 and 3/2+5*4"
text = " i like 555+42*232-123  5+2 6*9"
pattern = r"\b(?:\d+[\+\-\*\/])*\d+\b"
matches = re.findall(pattern, text)
print(matches)
