import nltk
from sklearn.feature_extraction.text import CountVectorizer

texts = [
"machine learning is powerful",
"data science is interesting"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(texts)

print(X.toarray())
