import re

def tokenize(input_text):
    words = re.findall(r'\b\w+\b|[^\w\s]', input_text)
    return words

input_text = "The quick, brown fox jumped over the lazy dog!"
tokens = tokenize(input_text)

print(tokens)