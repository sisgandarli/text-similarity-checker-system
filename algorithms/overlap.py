from algorithms.similarity_algorithms import SimilarityAlgorithm
import math
from algorithms.stemmer import Stemmer


class OverlapCoefSim(SimilarityAlgorithm):
    def compare(self, text_a, text_b):
        texta = self.split(self.lower(self.remove_punctuation(text_a)))
        textb = self.split(self.lower(self.remove_punctuation(text_b)))

        set_a = set(texta)
        set_b = set(textb)

        matching_coefficient = len(set_a & set_b) / (min(len(set_a), len(set_b)))

        return matching_coefficient


class OverlapCoefSimStem(SimilarityAlgorithm):
    def compare(self, text_a, text_b):
        texta = self.split(self.lower(self.remove_punctuation(text_a)))
        textb = self.split(self.lower(self.remove_punctuation(text_b)))

        stemmer = Stemmer()

        texta = stemmer.stem_words(texta)
        textb = stemmer.stem_words(textb)

        set_a = set(texta)
        set_b = set(textb)

        matching_coefficient = len(set_a & set_b) / (min(len(set_a), len(set_b)))

        return matching_coefficient


class OverlapCoefSimStemStopwordsRem(SimilarityAlgorithm):
    def compare(self, text_a, text_b):
        texta = self.split(self.lower(self.remove_punctuation(text_a)))
        textb = self.split(self.lower(self.remove_punctuation(text_b)))

        texta = self.remove_stopwords(texta)
        textb = self.remove_stopwords(textb)

        stemmer = Stemmer()

        texta = stemmer.stem_words(texta)
        textb = stemmer.stem_words(textb)

        set_a = set(texta)
        set_b = set(textb)

        matching_coefficient = len(set_a & set_b) / (min(len(set_a), len(set_b)))

        return matching_coefficient
