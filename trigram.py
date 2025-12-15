import nltk
from nltk.tokenize import word_tokenize
from nltk.util import trigrams

# Download tokenizer if needed
nltk.download('punkt')
nltk.download('punkt_tab')

text = "Natural Language Processing is very important in data science"

tokens = word_tokenize(text)
print("Tokens:")
print(tokens)

trigram_list = list(trigrams(tokens))

print("\nTrigrams:")
for tg in trigram_list:
    print(tg)
