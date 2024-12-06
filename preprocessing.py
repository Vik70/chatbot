# preprocessing.py
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Preprocess the text data by tokenizing, lowercasing, and removing stopwords
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return " ".join(tokens)
