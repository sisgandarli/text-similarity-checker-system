# -*- coding: utf-8 -*-

import string
import math

from algorithms.dice import *
from algorithms.cosine import *
from algorithms.jaccard import *
from algorithms.overlap import *

import pandas as pd
import os

df = pd.read_excel("../files/news.xlsx")
df["id"] = pd.to_numeric(df["id"])
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d %h:%M:%s")
df = df.sort_values(by='date')

myfile = "../files/train.csv"
if os.path.isfile(myfile):
    os.remove(myfile)

for i in range(len(df) // 1000 + 1):
    for j in range(i * 1000, i * 1000 + 1000):
        ind = [k for k in range(i * 1000, i * 1000 + 1000)]
        for a in range(len(ind)):
            for b in range(a + 1, len(ind)):
                texta = df.iloc[a][2]
                textb = df.iloc[b][2]

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

                res_list.append(m1.compare(texta, textb))
                res_list.append(m2.compare(texta, textb))
                res_list.append(m3.compare(texta, textb))
                res_list.append(m4.compare(texta, textb))
                res_list.append(m5.compare(texta, textb))
                res_list.append(m6.compare(texta, textb))
                res_list.append(m7.compare(texta, textb))
                res_list.append(m8.compare(texta, textb))
                res_list.append(m9.compare(texta, textb))
                res_list.append(m10.compare(texta, textb))
                res_list.append(m11.compare(texta, textb))
                res_list.append(m12.compare(texta, textb))

                with open("../files/train.csv", "a") as train_file:
                    train_file.write(str(res_list))
                    train_file.write("\n")

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
