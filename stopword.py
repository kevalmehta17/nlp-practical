import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# text = "Natural Language Processing is one of the most important areas in computer science"
text = """After India gained independence on 15 August 1947, Surat became part of India.
At that time it was a part of Bombay State.
Later it became the part of Gujarat State.
Along with Mumbai, Ahmedabad, Pune, Nagpur and Vadodara, Surat became one of the fast growing cities and major commercial and industrial centers of Western India.
During the post independence period, Surat has experienced considerable growth in industrial activities especially textiles and chemical along with trading activities."""

tokens = word_tokenize(text)
print("Original Tokens:")
print(tokens)


stop_words = set(stopwords.words('english'))

filtered_tokens = []
for word in tokens:
    if word.lower() not in stop_words:
        filtered_tokens.append(word)

print("\nAfter Stopword Removal:")
print(filtered_tokens)
