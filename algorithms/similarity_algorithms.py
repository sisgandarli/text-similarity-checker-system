import string
import math
from algorithms.stemmer import Stemmer


class SimilarityAlgorithm:
    stopwords = []

    def __init__(self):
        self.load_stopwords()

    def __del__(self):
        self.stopwords.clear()

    def load_stopwords(self):
        with open("files/stop-words-AZ.txt", "r", encoding="utf8") as stopwords_file:
            for word in stopwords_file:
                self.stopwords.append(word.strip())

    def lower(self, text):
        return text.lower()

    def split(self, text):
        return text.split()

    def remove_punctuation(self, text):
        return text.translate(text.maketrans(string.punctuation, " " * len(string.punctuation)))

    def remove_spec_chars(self, text):
        return text.replace(u'\xa0', u' ')

    def remove_stopwords(self, list_of_words):
        return [word for word in list_of_words if word not in self.stopwords]

    def compare(self, text_a, text_b):
        pass
