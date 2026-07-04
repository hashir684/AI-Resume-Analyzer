import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))


def clean_text(text: str) -> str:
    """
    Lowercase text and remove unwanted characters.
    Keeps skill-related symbols like + and #. """
    
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize_text(text: str) -> list:
    """
    Convert text into tokens
    """
    return word_tokenize(text)


def remove_stopwords(tokens: list) -> list:
    """
    Remove common English stopwords
    """
    return [
        word for word in tokens
        if word not in stop_words and len(word) > 2
    ]


def lemmatize_tokens(tokens: list) -> list:  
    return [lemmatizer.lemmatize(word) for word in tokens]


def preprocess_text(text: str) -> str:
    text = clean_text(text)
    tokens = tokenize_text(text)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize_tokens(tokens)

    return " ".join(tokens)


if __name__ == "__main__":
    sample_text = """
    Experienced Python Developer with 3+ years of experience in
    Machine Learning, NLP, FastAPI, and SQL.
    """
    print(preprocess_text(sample_text))
