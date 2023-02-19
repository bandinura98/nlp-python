import nltk
from nltk.stem import KrovetzStemmer

# Create a Krovetz stemmer object
krovetz = KrovetzStemmer()

# Example words to stem
words = ['running', 'runs', 'ran', 'jumping', 'jumps', 'jumped']

# Apply the Krovetz stemmer to each word
stemmed_words = [krovetz.stem(word) for word in words]

# Print the stemmed words
print(stemmed_words)