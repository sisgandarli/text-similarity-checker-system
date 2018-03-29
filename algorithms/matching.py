from algorithms.similarity_algorithms import SimilarityAlgorithm
import math
from algorithms.stemmer import Stemmer


class MatchingCoefSim(SimilarityAlgorithm):
    def compare(self, text_a, text_b):
        texta = self.split(self.lower(self.remove_punctuation(text_a)))
        textb = self.split(self.lower(self.remove_punctuation(text_b)))

        general_set = set()
        for i in texta:
            general_set.add(i)
        for i in textb:
            general_set.add(i)

        map_a = {}
        map_b = {}
        for i in general_set:
            map_a[i] = 0
            map_b[i] = 0

        for i in texta:
            map_a[i] = 1
        for i in textb:
            map_b[i] = 1

        m00 = 0
        m01 = 0
        m10 = 0
        m11 = 0

        for i in general_set:
            if map_a[i] == 0 and map_b[i] == 0:
                m00 += 1
            elif map_a[i] == 0 and map_b[i] == 1:
                m01 += 1
            if map_a[i] == 1 and map_b[i] == 0:
                m10 += 1
            if map_a[i] == 1 and map_b[i] == 1:
                m11 += 1

        matching_coefficient = (m00 + m11) / (m00 + m01 + m10 + m11)

        return matching_coefficient


class MatchingCoefStem(SimilarityAlgorithm):
    def compare(self, text_a, text_b):
        texta = self.split(self.lower(self.remove_punctuation(text_a)))
        textb = self.split(self.lower(self.remove_punctuation(text_b)))

        stemmer = Stemmer()

        texta = stemmer.stem_words(texta)
        textb = stemmer.stem_words(textb)

        general_set = set()
        for i in texta:
            general_set.add(i)
        for i in textb:
            general_set.add(i)

        map_a = {}
        map_b = {}
        for i in general_set:
            map_a[i] = 0
            map_b[i] = 0

        for i in texta:
            map_a[i] = map_a[i] + 1
        for i in textb:
            map_b[i] = map_b[i] + 1

        m00 = 0
        m01 = 0
        m10 = 0
        m11 = 0

        for i in general_set:
            if map_a[i] == 0 and map_b[i] == 0:
                m00 += 1
            elif map_a[i] == 0 and map_b[i] == 1:
                m01 += 1
            if map_a[i] == 1 and map_b[i] == 0:
                m10 += 1
            if map_a[i] == 1 and map_b[i] == 1:
                m11 += 1

        matching_coefficient = (m00 + m11) / (m00 + m01 + m10 + m11)

        return matching_coefficient


class MatchingCoefSimStemStopwordsRem(SimilarityAlgorithm):
    def compare(self, text_a, text_b):
        texta = self.split(self.lower(self.remove_punctuation(text_a)))
        textb = self.split(self.lower(self.remove_punctuation(text_b)))

        texta = self.remove_stopwords(texta)
        textb = self.remove_stopwords(textb)

        stemmer = Stemmer()

        texta = stemmer.stem_words(texta)
        textb = stemmer.stem_words(textb)

        general_set = set()
        for i in texta:
            general_set.add(i)
        for i in textb:
            general_set.add(i)

        map_a = {}
        map_b = {}
        for i in general_set:
            map_a[i] = 0
            map_b[i] = 0

        for i in texta:
            map_a[i] = map_a[i] + 1
        for i in textb:
            map_b[i] = map_b[i] + 1

        m00 = 0
        m01 = 0
        m10 = 0
        m11 = 0

        for i in general_set:
            if map_a[i] == 0 and map_b[i] == 0:
                m00 += 1
            elif map_a[i] == 0 and map_b[i] == 1:
                m01 += 1
            if map_a[i] == 1 and map_b[i] == 0:
                m10 += 1
            if map_a[i] == 1 and map_b[i] == 1:
                m11 += 1

        matching_coefficient = (m00 + m11) / (m00 + m01 + m10 + m11)

        return matching_coefficient
