import nltk
from nltk.stem import PorterStemmer

# Create a Porter stemmer object
porter = PorterStemmer()

# Example words to stem
words = ['running', 'runs', 'ran', 'jumping', 'jumps', 'jumped']

# Apply the Porter stemmer to each word
stemmed_words = [porter.stem(word) for word in words]

# Print the stemmed words
print(stemmed_words)