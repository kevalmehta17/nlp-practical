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


# OR code using manual implementation of Lesk Algorithm

# import nltk
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('punkt')

# from nltk.corpus import wordnet as wn
# from nltk.tokenize import word_tokenize

# def lesk_algorithm(sentence, target_word):
#     # Tokenize and lowercase context
#     context = set(word_tokenize(sentence.lower()))
    
#     max_overlap = 0
#     best_sense = None

#     # Iterate through all possible senses
#     for sense in wn.synsets(target_word):
#         # Tokenize definition (gloss)
#         gloss = set(word_tokenize(sense.definition().lower()))

#         # Calculate overlap
#         overlap = len(context.intersection(gloss))

#         if overlap > max_overlap:
#             max_overlap = overlap
#             best_sense = sense

#     return best_sense

# sentence = "He went to the bank to deposit money"
# target_word = "bank"

# sense = lesk_algorithm(sentence, target_word)
# print("Best Sense:", sense)
# print("Definition:", sense.definition())


