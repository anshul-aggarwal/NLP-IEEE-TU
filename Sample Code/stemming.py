import nltk
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
words = ['caresses', 'ponies', 'caress','cats']
for word in words:
    print(word, "->", stemmer.stem(word))
