# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import os


myfile="../files/train_final.csv"
if os.path.isfile(myfile):
    os.remove(myfile)

with open("../files/train.csv", "r") as rd:
    with open("../files/train_final.csv", "a") as wr:
        for i in range(1, 13):
            wr.write("x" + str(i))
            if (i != 12): wr.write(",")
        wr.write("\n")
        for line in rd:
            line = line.strip()
            if (line.startswith("[")):
                line = line[1:len(line)]
            if (line.endswith("]")):
                line = line[:len(line) - 1]
            wr.write(line + "\n")



train = pd.read_csv("../files/train_final.csv")
train["x1"] = pd.to_numeric(train["x1"], errors='coerce')
train["x2"] = pd.to_numeric(train["x2"], errors='coerce')
train["x3"] = pd.to_numeric(train["x3"], errors='coerce')
train["x4"] = pd.to_numeric(train["x4"], errors='coerce')
train["x5"] = pd.to_numeric(train["x5"], errors='coerce')
train["x6"] = pd.to_numeric(train["x6"], errors='coerce')
train["x7"] = pd.to_numeric(train["x7"], errors='coerce')
train["x8"] = pd.to_numeric(train["x8"], errors='coerce')
train["x9"] = pd.to_numeric(train["x9"], errors='coerce')
train["x10"] = pd.to_numeric(train["x10"], errors='coerce')
train["x11"] = pd.to_numeric(train["x11"], errors='coerce')
train["x12"] = pd.to_numeric(train["x12"], errors='coerce')



train["y"] = (train["x1"] >= 0.5) | (train["x2"] >= 0.5) | (train["x3"] >= 0.5) | (train["x4"] >= 0.5) | (train["x5"] >= 0.5) | (train["x6"] >= 0.5) | (train["x7"] >= 0.5) | (train["x8"] >= 0.5) | (train["x9"] >= 0.5) | (train["x10"] >= 0.5) | (train["x11"] >= 0.5) | (train["x12"] >= 0.5) 
train[["y"]] *= 1

myfile="../files/train_finalized.csv"
if os.path.isfile(myfile):
    os.remove(myfile)

train.to_csv("../files/train_finalized.csv", index=False)

