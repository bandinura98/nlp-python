def tokenize(input_text):
    return input_text.split()

input_text = "The quick brown fox jumped over the lazy dog."
tokens = tokenize(input_text)

print(tokens)