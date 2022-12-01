# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import os
import pandas as pd


with open("Inputs/inputDay1.txt") as f:
    # Getting the first line as the "bingo balls"
    data = np.array(f.readlines())


puzInput = [d.replace('\n','') for d in data]

elfCalories = []
cumul = 0
for i in puzInput:
    if i != '':
        cumul += int(i)
    else:
        elfCalories.append(cumul)
        cumul=0

print("part 1:", max(elfCalories))

# Part 2
sortedCalories = elfCalories.copy()
sortedCalories.sort(reverse=True)
totalTop3 = sum(sortedCalories[0:3])

print('part 2', totalTop3)