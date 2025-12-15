# Tokenize

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download required tokenizer model (run once)
nltk.download('punkt')

text = """
Natural Language Processing is a fascinating field.
It allows machines to understand human language.
Tokenization is the first step in NLP.
NLTK provides simple tools for tokenization.
This experiment demonstrates sentence and word tokenization.
"""

sentences = sent_tokenize(text)

print("Sentence Tokens:")
for i, s in enumerate(sentences, 1):
    print(f"{i}. {s}")

print("\nWord Tokens:")
for i, s in enumerate(sentences, 1):
    print(f"Sentence {i} tokens:", word_tokenize(s))
