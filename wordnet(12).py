import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')


words = ["good", "run", "computer", "happy", "bank"]



for word in words:
    print(f"\nWord: {word}")
    synsets = wn.synsets(word)

    if synsets:
        print("Definition:", synsets[0].definition())
        print("Synonyms:", synsets[0].lemma_names())

