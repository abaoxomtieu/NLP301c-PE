import re

document = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."

pattern = r'\b\w+\b|[.]'
tokens = re.findall(pattern, document)
# print(tokens)
array = []
final_array = []
for token in tokens:
    if (token!= "."):
        array.append(token)
    else:
        array[len(array)-1] = array[len(array)-1] + token
        final_array.append(" ".join(array))
        array = []
for string in final_array:
    print(string)