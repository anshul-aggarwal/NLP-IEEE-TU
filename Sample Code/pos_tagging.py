import nltk
from nltk import word_tokenize
txt = "Hello my name is John Doe and my favourite number is twenty-seven"
tokens = word_tokenize(txt)
pos = nltk.pos_tag(tokens)
print(pos)
