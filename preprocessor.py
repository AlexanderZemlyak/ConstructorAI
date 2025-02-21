from sklearn.base import BaseEstimator, TransformerMixin
import nltk
import pymorphy3
import string
import re

class CleanTextTransformer(BaseEstimator, TransformerMixin):

    def __init__(self):
        self.ma = pymorphy3.MorphAnalyzer()

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return [str(self.clean_text(text)) for text in X]

    def remove_punctuation(self, text):
      text_nopunct = "".join([char for char in text if char not in string.punctuation])
      return text_nopunct

    def tokenise(self, text):
      tokens = re.split('\W+', text)
      return tokens

    def remove_stopwords(self, tokenised_list):
      stopwords = nltk.corpus.stopwords.words('russian')
      filtered_text = [word for word in tokenised_list if word not in stopwords]
      return filtered_text

    def stemming(self, tokenised_text):
      ps = nltk.SnowballStemmer('russian')
      processed_text = [ps.stem(word) for word in tokenised_text]
      return processed_text

    def lemmatizing(self, tokenized_text):
      processed_text = [self.ma.parse(word)[0].normal_form for word in tokenized_text]
      return processed_text

    def clean_text(self, text):
      text = self.remove_punctuation(text)
      tokens = self.tokenise(text)
      processed_text = self.lemmatizing(tokens)
      return processed_text