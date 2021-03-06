from algorithms.similarity_algorithms import SimilarityAlgorithm
import math
from algorithms.stemmer import Stemmer


class JaccardSim(SimilarityAlgorithm):
    def compare(self, text_a, text_b):
        texta = self.split(self.lower(self.remove_punctuation(self.remove_spec_chars(text_a))))
        textb = self.split(self.lower(self.remove_punctuation(self.remove_spec_chars(text_b))))

        set_a = set(texta)
        set_b = set(textb)

        jaccard_similarity_result = len(set_a & set_b) / len(set_a | set_b)

        return jaccard_similarity_result


class JaccardSimStem(SimilarityAlgorithm):
    def compare(self, text_a, text_b):
        texta = self.split(self.lower(self.remove_punctuation(self.remove_spec_chars(text_a))))
        textb = self.split(self.lower(self.remove_punctuation(self.remove_spec_chars(text_b))))

        stemmer = Stemmer()

        texta = stemmer.stem_words(texta)
        textb = stemmer.stem_words(textb)

        set_a = set(texta)
        set_b = set(textb)

        jaccard_similarity_result = len(set_a & set_b) / len(set_a | set_b)

        return jaccard_similarity_result


class JaccardSimStemStopwordsRem(SimilarityAlgorithm):
    def compare(self, text_a, text_b):
        texta = self.split(self.lower(self.remove_punctuation(self.remove_spec_chars(text_a))))
        textb = self.split(self.lower(self.remove_punctuation(self.remove_spec_chars(text_b))))

        texta = self.remove_stopwords(texta)
        textb = self.remove_stopwords(textb)

        stemmer = Stemmer()

        texta = stemmer.stem_words(texta)
        textb = stemmer.stem_words(textb)

        set_a = set(texta)
        set_b = set(textb)

        jaccard_similarity_result = len(set_a & set_b) / len(set_a | set_b)

        return jaccard_similarity_result
