from nltk.tokenize import word_tokenize, sent_tokenize
print("---WORD TOKENIZATION---")
sentence = "The process of segmenting text into independent words."
words = word_tokenize(sentence)
print(words)
paragraph = "His name is Mr. John Doe. He is a professional cricket player."
sentences = sent_tokenize(paragraph)
print("---SENTENCE TOKENIZATION---")
for sent in sentences:
    print(sent)
