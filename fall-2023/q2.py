import re
s = ' this is. \n a sample \t. sentence'
pattern = r'\b\w*\S\b'
match = re.findall(pattern,s)
print(" ".join(match))