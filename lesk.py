import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')


sentence = "He went to the bank to deposit money"
ambiguous_word = "bank"
sense = lesk(sentence.split(), ambiguous_word)

print("Sentence:", sentence)
print("Ambiguous word:", ambiguous_word)

if sense:
    print("\nSelected Synset:", sense.name())
    print("Definition:", sense.definition())
else:
    print("No sense found")