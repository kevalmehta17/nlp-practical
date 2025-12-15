from nltk.stem import PorterStemmer

words = [
    "connect", "connected", "connecting", "connection",
    "studies", "studying", "studied",
    "running", "runner", "runs"
]
ps = PorterStemmer()

stemmed_words = []

for word in words:
    stem = ps.stem(word)
    stemmed_words.append(stem)
    
print("Original Words:")
print(words)

print("\nAfter Porter Stemming:")
print(stemmed_words)