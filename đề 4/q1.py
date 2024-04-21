import re
text = " iam zboy zick zack and play boy of genz z"
pattern = r"\b\w*z\w*\b"
match = re.findall(pattern, text)
print(match)