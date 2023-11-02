import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download NLTK data (if you haven't already)
nltk.download('punkt')
nltk.download('wordnet')

# Sample text
text = "The quick brown foxes jumped over the lazy dogs. Running and ran are forms of run."

# Tokenize the text into words
words = word_tokenize(text)

# Initialize a Porter Stemmer
stemmer = PorterStemmer()

# Initialize a WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()

# Perform morphological analysis
print("Token\tStem\tLemma")
for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print(f"{word}\t{stem}\t{lemma}")
