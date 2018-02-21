import string
import math


class SimilarityAlgorithm:
    def lower(self, text):
        return text.lower()

    def split(self, text):
        return text.split()

    def remove_punctuation(self, text):
        return text.translate(text.maketrans(string.punctuation, " " * len(string.punctuation)))

    def compare(self, text_a, text_b):
        pass


class CosineSimilarityAlgorithm(SimilarityAlgorithm):
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
            ab += map_a[i] * map_b[i]
        for i in general_set:
            a += map_a[i] ** 2
        for i in general_set:
            b += map_b[i] ** 2

        cosine_similarity_coefficient = ab / (math.sqrt(a) * math.sqrt(b))

        return cosine_similarity_coefficient


class JaccardSimilarityAlgorithm(SimilarityAlgorithm):
    def compare(self, text_a, text_b):
        texta = self.split(self.lower(self.remove_punctuation(text_a)))
        textb = self.split(self.lower(self.remove_punctuation(text_b)))

        set_a = set(texta)
        set_b = set(textb)

        jaccard_similarity_result = len(set_a & set_b) / len(set_a | set_b)

        return jaccard_similarity_result
