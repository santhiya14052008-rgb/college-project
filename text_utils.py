import re


def split_terms(text):
    """
    Split text into useful search terms.
    """

    if not text:
        return []

    text = str(text).lower()

    # Remove punctuation
    text = re.sub(r"[^\w\s]", " ", text)

    # Split into words
    terms = text.split()

    # Remove duplicates while preserving order
    return list(dict.fromkeys(terms))