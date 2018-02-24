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

    def remove_stopwords(self, list_of_words):
        for word in list_of_words:
            if word in self.stopwords:
                list_of_words.remove(word)
        return list_of_words

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


class CosineSimilarityAlgorithmWithStemming(SimilarityAlgorithm):
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
            ab += map_a[i] * map_b[i]
        for i in general_set:
            a += map_a[i] ** 2
        for i in general_set:
            b += map_b[i] ** 2

        cosine_similarity_coefficient = ab / (math.sqrt(a) * math.sqrt(b))

        return cosine_similarity_coefficient


class CosineSimilarityAlgorithmWithStemmingStopwordsRemoved(SimilarityAlgorithm):
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


class JaccardSimilarityAlgorithmWithStemming(SimilarityAlgorithm):
    def compare(self, text_a, text_b):
        texta = self.split(self.lower(self.remove_punctuation(text_a)))
        textb = self.split(self.lower(self.remove_punctuation(text_b)))

        stemmer = Stemmer()

        texta = stemmer.stem_words(texta)
        textb = stemmer.stem_words(textb)

        set_a = set(texta)
        set_b = set(textb)

        jaccard_similarity_result = len(set_a & set_b) / len(set_a | set_b)

        return jaccard_similarity_result


class JaccardSimilarityAlgorithmWithStemmingStopwordsRemoved(SimilarityAlgorithm):
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

        jaccard_similarity_result = len(set_a & set_b) / len(set_a | set_b)

        return jaccard_similarity_result
