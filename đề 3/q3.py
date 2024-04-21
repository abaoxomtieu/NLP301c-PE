import re
import string
text = "Reset your password if you just can't remember your old one. ? @@"
pattern = r"\b\w+\b|[" + string.punctuation + "]"
token = re.findall(pattern, text)
print(token)
# print(string.punctuation)