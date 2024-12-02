import re

def clean_text(text):
    
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Remove special characters, digits, and punctuation
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Convert to lowercase
    text = text.lower()

    # Remove extra whitespaces
    text = re.sub(r"\s+", " ", text).strip()

    return text
