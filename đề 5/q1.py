import re
text = " I like python and pt on my school, i train model wwith filept lern tensorflow and pt, lenpt"
pattern = r'\b\w*pt\w*\b'
match = re.findall(pattern,text)
print(match)