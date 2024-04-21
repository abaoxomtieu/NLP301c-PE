import re

document = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."

pattern = r'\b\w+\b|[.]'
tokens = re.findall(pattern, document)
# print(tokens)
array = []
for token in tokens:
    if (token!= "."):
        array.append(token)
    else:
        array.append(token)
        print(array)
        array = []
    