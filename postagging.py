import nltk

# Download required resources (run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

from nltk import word_tokenize, pos_tag


sentence = "NLTK is a powerful library for natural language processing."

tokens = word_tokenize(sentence)

pos_tags = pos_tag(tokens)

print("English POS Tags:")
print(pos_tags)

# for indian language

import nltk
from nltk.corpus import indian

# Download Indian corpus (run once)
nltk.download('indian')

# Load Hindi tagged sentences
hindi_sentences = indian.tagged_sents('hindi.pos')

# Print first sentence with POS tags
print("Hindi POS Tags:")
print(hindi_sentences[0])
