import nltk
from nltk.tokenize import word_tokenize
from nltk.util import bigrams

# Download tokenizer if needed
nltk.download('punkt')
nltk.download('punkt_tab')

text = "Natural Language Processing is very important in data science"

tokens = word_tokenize(text)
print("Tokens:")
print(tokens)


bigram_list = list(bigrams(tokens))

print("\nBigrams:")
for bg in bigram_list:
    print(bg)
