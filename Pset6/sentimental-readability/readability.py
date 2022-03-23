# TODO: if you never used nltk before, you should probably import nltk and run "nltk.download("punkt")"
from nltk import tokenize

text = input("Text: ")

# letters per 100 words
letter = 0
for char in text:
    if char.isalpha():
        letter += 1

# Number of words in the sentence
words = len(text.split(" "))

# Letters per 100 words
L = round((letter/words)*100, 2)

# separate the sentences
sentences = len(tokenize.sent_tokenize(text))
# sentences per 100 words
S = round((sentences/words)*100, 2)

# index equation
index = 0.0588 * L - 0.296 * S - 15.8
if 1 > round(index):
    print(f"Before Grade 1")
elif round(index) >= 16:
    print("Grade 16+")
else:
    print(f"Grade {round(index)}")

