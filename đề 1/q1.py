# define s as a text, write expresison for finding all words in s that all lowercase letters. The result should be in the form of a list of words: ['word1],'word2',...]

import re
s = 'This is a test. 123. Hello World. 1 2 3 du ma lon so roi nha'
print(re.findall(r'\b[a-z]+\b', s))
