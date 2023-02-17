import re

def tokenize(input_text, pattern):
    words = re.findall(pattern, input_text)
    return words

input_text = "The quick brown fox jumped over the lazy dog."
pattern = r'\b\w+\b'

tokens = tokenize(input_text, pattern)

print(tokens)