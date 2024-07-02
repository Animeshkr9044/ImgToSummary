import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


def preprocess_text(text):
    """
    Preprocesses text using tokenization, lowercasing, punctuation removal, stop word removal, stemming, and lemmatization.

    Args:
        text (str): The text to be preprocessed.

    Returns:
        str: The preprocessed text.
    """
    # 1. Tokenization
    words = nltk.word_tokenize(text)

    # 2. Lowercasing
    words = [word.lower() for word in words]

    # 3. Removing Punctuation
    words = [word for word in words if word.isalnum()]

    # 4. Removing Stop Words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # 5. Stemming
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]

    # 6. Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in stemmed_words]

    # Join processed words into a single string
    processed_text = ' '.join(lemmatized_words)

    return processed_text
