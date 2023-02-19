import nltk
from nltk.stem import LancasterStemmer

# Create a Lancaster stemmer object
lancaster = LancasterStemmer()

# Example words to stem
words = ['running', 'runs', 'ran', 'jumping', 'jumps', 'jumped']

# Apply the Lancaster stemmer to each word
stemmed_words = [lancaster.stem(word) for word in words]

# Print the stemmed words
print(stemmed_words)