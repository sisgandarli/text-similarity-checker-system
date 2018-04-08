from algorithms.similarity_algorithms import SimilarityAlgorithm
import math
from algorithms.stemmer import Stemmer


class CosineSim(SimilarityAlgorithm):
    def compare(self, text_a, text_b):
        texta = self.split(self.lower(self.remove_punctuation(self.remove_spec_chars(text_a))))
        textb = self.split(self.lower(self.remove_punctuation(self.remove_spec_chars(text_b))))

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
            ab += map_a[i] * map_b[i]
        for i in general_set:
            a += map_a[i] ** 2
        for i in general_set:
            b += map_b[i] ** 2

        cosine_similarity_coefficient = ab / (math.sqrt(a) * math.sqrt(b))

        return cosine_similarity_coefficient


class CosineSimStem(SimilarityAlgorithm):
    def compare(self, text_a, text_b):
        texta = self.split(self.lower(self.remove_punctuation(self.remove_spec_chars(text_a))))
        textb = self.split(self.lower(self.remove_punctuation(self.remove_spec_chars(text_b))))

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
            ab += map_a[i] * map_b[i]
        for i in general_set:
            a += map_a[i] ** 2
        for i in general_set:
            b += map_b[i] ** 2

        cosine_similarity_coefficient = ab / (math.sqrt(a) * math.sqrt(b))

        return cosine_similarity_coefficient


class CosineSimStemStopwordsRem(SimilarityAlgorithm):
    def compare(self, text_a, text_b):
        texta = self.split(self.lower(self.remove_punctuation(self.remove_spec_chars(text_a))))
        textb = self.split(self.lower(self.remove_punctuation(self.remove_spec_chars(text_b))))

        texta = self.remove_stopwords(texta)
        textb = self.remove_stopwords(textb)
        var_1 = text_a
        var_2 = text_b

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
            ab += map_a[i] * map_b[i]
        for i in general_set:
            a += map_a[i] ** 2
        for i in general_set:
            b += map_b[i] ** 2

        cosine_similarity_coefficient = ab / (math.sqrt(a) * math.sqrt(b))

        return cosine_similarity_coefficient
