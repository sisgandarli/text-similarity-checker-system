from algorithms.similarity_algorithms import SimilarityAlgorithm
import math
from algorithms.stemmer import Stemmer


class DiceSim(SimilarityAlgorithm):
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
            map_a[i] = map_a[i] + 1
        for i in textb:
            map_b[i] = map_b[i] + 1

        ab = 0
        a = 0
        b = 0
        for i in general_set:
            if map_a[i] > 0 and map_b[i] > 0:
                ab += 1
        for i in general_set:
            if map_a[i] > 0:
                a += 1
            if map_b[i] > 0:
                b += 1

        dice_similarity_coefficient = (2 * ab) / (a + b)

        return dice_similarity_coefficient


class DiceSimStemming(SimilarityAlgorithm):
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

        ab = 0
        a = 0
        b = 0
        for i in general_set:
            if map_a[i] > 0 and map_b[i] > 0:
                ab += 1
        for i in general_set:
            if map_a[i] > 0:
                a += 1
            if map_b[i] > 0:
                b += 1

        dice_similarity_coefficient = (2 * ab) / (a + b)

        return dice_similarity_coefficient


class DiceSimStemmingWithoutStopwords(SimilarityAlgorithm):
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

        ab = 0
        a = 0
        b = 0
        for i in general_set:
            if map_a[i] > 0 and map_b[i] > 0:
                ab += 1
        for i in general_set:
            if map_a[i] > 0:
                a += 1
            if map_b[i] > 0:
                b += 1

        dice_similarity_coefficient = (2 * ab) / (a + b)

        return dice_similarity_coefficient
