import re
text = "generlize ize is best thing of GPT it specialize features summarize"
pattern = r"\b\w+ize\b"
token = re.findall(pattern, text)
print(token)