import jieba

# Input text
text = "我喜欢吃水果"

# Perform word segmentation
words = jieba.cut(text)

# Print the segmented words
for word in words:
    print(word)