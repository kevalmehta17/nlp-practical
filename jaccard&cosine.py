import spacy
import numpy as np

nlp = spacy.load("en_core_web_sm")

text1 = "Natural language processing is very interesting"
text2 = "Natural language processing is extremely fascinating"

doc1 = nlp(text1)
doc2 = nlp(text2)

set1 = set([token.text.lower() for token in doc1 if token.is_alpha])
set2 = set([token.text.lower() for token in doc2 if token.is_alpha])

intersection = set1.intersection(set2)
union = set1.union(set2)

jaccard_similarity = len(intersection) / len(union)

print("Jaccard Similarity:", jaccard_similarity)


cosine_similarity = doc1.similarity(doc2)
print("Cosine Similarity:", cosine_similarity)
