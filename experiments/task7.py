import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Downloads (sirf 1 dafa run karna hai)
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")

text = "Artificial Intelligence is transforming the world. Machine Learning is a subset of AI."

# 1. Tokenize
tokens = word_tokenize(text)
print("Tokens:", tokens)

# 2. Remove stopwords
stop_words = set(stopwords.words("english"))
filtered_tokens = [w for w in tokens if w.lower() not in stop_words and w.isalpha()]
print("Filtered Tokens:", filtered_tokens)

# 3. POS Tagging
pos_tags = pos_tag(filtered_tokens)
print("POS Tags:", pos_tags)

# 4. Extract Nouns
nouns = [word for word, tag in pos_tags if tag.startswith("NN")]
print("Nouns:", nouns)
