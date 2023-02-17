import nltk
from nltk.tokenize import MaxentTokenizer

# Sample input text
input_text = "The quick brown fox jumped over the lazy dog."

# Instantiate a MaxEnt Tokenizer
maxent_tokenizer = MaxentTokenizer()

# Tokenize the input text
tokens = maxent_tokenizer.tokenize(input_text)

# Print the list of tokens
print(tokens)