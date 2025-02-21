import nltk
import pymorphy3
import string
import re

ma = pymorphy3.MorphAnalyzer()

def remove_punctuation(text):
    text_nopunct = "".join([char for char in text if char not in string.punctuation])
    return text_nopunct

def tokenise(text):
    tokens = re.split('\W+', text)
    return tokens

def remove_stopwords(tokenised_list):
    stopwords = nltk.corpus.stopwords.words('russian')
    filtered_text = [word for word in tokenised_list if word not in stopwords]
    return filtered_text

def stemming(tokenised_text):
    ps = nltk.SnowballStemmer('russian')
    processed_text = [ps.stem(word) for word in tokenised_text]
    return processed_text

def lemmatizing(tokenized_text):
    processed_text = [ma.parse(word)[0].normal_form for word in tokenized_text]
    return processed_text

def clean_text(text):
    text = remove_punctuation(text)
    tokens = tokenise(text)
    processed_text = lemmatizing(tokens)
    return processed_text