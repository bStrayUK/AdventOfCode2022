# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 12:48:32 2022

@author: straybj
"""


import numpy as np

with open("Inputs/inputDay2.txt") as f:
    data = np.array(f.readlines())

opponent = []
response = []
for i in data:
    opponent.append(i[0])
    response.append(i[2])

    
numberDict = {'X':1,'Y':2,'Z':3}
letterDict = {'A':'X','B':'Y','C':'Z'}

sumPlaying = 0
sumWinning = 0
sumTotal = 0

# for index,value in enumerate(response):
for index,value in enumerate(response[0:30]):
    sumPlaying += numberDict[value]
    sumTotal += numberDict[value]
    print(letterDict[opponent[index]],value)
    if letterDict[opponent[index]] == value:
        sumWinning +=3 #Draw condition
        sumTotal += 3 
        print("Draw, total ", sumTotal)
    elif value == 'X' and opponent[index] == "C":
        sumWinning += 6
        sumTotal += 6
        
        print("Win, total ", sumTotal)
    else: 
        if numberDict[value] > numberDict[letterDict[opponent[index]]]:
            sumWinning += 6
            sumTotal += 6
            print("Win, total ", sumTotal)
        else:
            print('Lose, total ', sumTotal)

        
totalScore = sumPlaying + sumWinning

print("Total score ", totalScore)
print("Total score ", sumTotal)


fullDict = {
    'AX' : 4,
    'AY' : 8,
    'AZ' : 3,
    'BX' : 1,
    'BY' : 5,
    'BZ' : 9,
    'CX' : 7,
    'CY' : 2,
    'CZ' : 6
    }

total = 0

for i,v in enumerate(opponent):
    total += fullDict[opponent[i]+response[i]]

print(total)

total2 = 0
fullDict2 = {
    'AX' : 3,
    'AY' : 4,
    'AZ' : 8,
    'BX' : 1,
    'BY' : 5,
    'BZ' : 9,
    'CX' : 2,
    'CY' : 6,
    'CZ' : 7
    }

for i,v in enumerate(opponent):
    total2 += fullDict2[opponent[i]+response[i]]
print(total2)