import nltk
from nltk.stem import WordNetLemmatizer

# Download required resource (run once)
nltk.download('wordnet')

words = [
    "running", "runs", "ran",
    "better", "best",
    "studies", "studying",
    "children", "mice"
]

lemmatizer = WordNetLemmatizer()

lemmatized_words = []

for word in words:
    lemma = lemmatizer.lemmatize(word)
    lemmatized_words.append(lemma)

print("Original Words:")
print(words)

print("\nAfter Lemmatization:")
print(lemmatized_words)
