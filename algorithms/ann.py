from algorithms.similarity_algorithms import SimilarityAlgorithm
import math
from algorithms.dice import *
from algorithms.cosine import *
from algorithms.overlap import *
from algorithms.jaccard import *
import pickle


class ANN(SimilarityAlgorithm):
    filename = "files/ann_model.sav"

    def compare(self, text_a, text_b):
        loaded_model = pickle.load(open(self.filename, "rb"))

        m1 = CosineSim()
        m2 = CosineSimStem()
        m3 = CosineSimStemStopwordsRem()
        m4 = JaccardSim()
        m5 = JaccardSimStem()
        m6 = JaccardSimStemStopwordsRem()
        m7 = DiceSim()
        m8 = DiceSimStem()
        m9 = DiceSimStemStopwordsRem()
        m10 = OverlapCoefSim()
        m11 = OverlapCoefSimStem()
        m12 = OverlapCoefSimStemStopwordsRem()

        res_list = []

        res_list.append(m1.compare(text_a, text_b))
        res_list.append(m2.compare(text_a, text_b))
        res_list.append(m3.compare(text_a, text_b))
        res_list.append(m4.compare(text_a, text_b))
        res_list.append(m5.compare(text_a, text_b))
        res_list.append(m6.compare(text_a, text_b))
        res_list.append(m7.compare(text_a, text_b))
        res_list.append(m8.compare(text_a, text_b))
        res_list.append(m9.compare(text_a, text_b))
        res_list.append(m10.compare(text_a, text_b))
        res_list.append(m11.compare(text_a, text_b))
        res_list.append(m12.compare(text_a, text_b))

        result = loaded_model.predict([res_list])

        del res_list
        del m1
        del m2
        del m3
        del m4
        del m5
        del m6
        del m7
        del m8
        del m9
        del m10
        del m11
        del m12

        if (result[0] == 1):
            return "Similar"
        else:
            return "Not Similar"
