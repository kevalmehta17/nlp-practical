import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')


words = ['good', 'bank', 'happy', 'great']

for word in words:
    print(f"\n==============================")
    print(f"Word: {word}")
    print("==============================")

    synsets = wn.synsets(word)

    for syn in synsets[:2]:   # limit output (exam-friendly)
        print("\nSynset:", syn.name())
        print("Definition:", syn.definition())

        # Synonyms
        print("Synonyms:", syn.lemma_names())

        # Antonyms
        antonyms = []
        for lemma in syn.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
        print("Antonyms:", antonyms if antonyms else "None")

        # Hypernyms
        print("Hypernyms:", [h.name() for h in syn.hypernyms()])

        # Hyponyms
        print("Hyponyms:", [h.name() for h in syn.hyponyms()])
