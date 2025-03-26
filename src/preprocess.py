import re
from nltk.tokenize import sent_tokenize

# Clean text by removing unnecessary characters
def clean_text(text):
    text = re.sub(r"[^a-zA-Z0-9\s.,!?']", " ", text)  # Allow basic punctuation
    text = re.sub(r'\s+', ' ', text).strip()          # Remove extra spaces
    return text

# Tokenize text into sentences
def tokenize_sentences(text):
    return sent_tokenize(text)
