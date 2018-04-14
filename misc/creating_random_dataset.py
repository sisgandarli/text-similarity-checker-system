# -*- coding: utf-8 -*-
import os
from random import random

myfile = "../files/train_random_data.csv"
if os.path.isfile(myfile):
    os.remove(myfile)

with open(myfile, "a") as f:
    for i in range(12):
        f.write("x"+str(i + 1)+",")
    f.write("y\n")
    
    for i in range(100000 // 2):
        for j in range(12):
            val = random() / 2
            f.write(str(val))
            f.write(",")
            del val
        f.write("0\n")
        for j in range(12):
            val = random() / 2 + 0.5
            f.write(str(val))
            f.write(",")
            del val
        f.write("1\n")
            