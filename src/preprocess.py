import re

URL_PATTERN = re.compile(r"http\S+|www\.\S+")
HTML_PATTERN = re.compile(r"<.*?>")

def clean_text(text: str) -> str:
    text = text.lower()
    text = URL_PATTERN.sub("", text)
    text = HTML_PATTERN.sub("", text)
    return text.strip()
