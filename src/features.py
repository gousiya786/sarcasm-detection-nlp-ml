import re
from sklearn.feature_extraction.text import CountVectorizer

ALL_CAPS_PATTERN = re.compile(r"\b[A-Z]{2,}\b")

def build_vectorizer(max_features=5000):
    return CountVectorizer(max_features=max_features, ngram_range=(1, 1))

def has_all_caps(text: str) -> int:
    return 1 if ALL_CAPS_PATTERN.search(text) else 0
