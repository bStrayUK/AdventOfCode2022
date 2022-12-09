# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:20:24 2022

@author: straybj
"""


with open("Inputs/inputDay5.txt") as f:
    data = f.readlines()
    
# read the stacks into strings and put in dictionaries
# Stack number is on line 8

stackDict = {}

for i, stackNum in enumerate(data[8]):
    if ((i-1)%4)==0:
        dummystr = ''
        for j,stackLine in enumerate(data[0:8]):
            dummystr += stackLine[i]
        
        stackDict[stackNum] = dummystr[::-1].strip()

print(stackDict)

stackDict2 = stackDict.copy()

# Part 1
# get the instructions. Can use .split()

for index, instr in enumerate(data[10::]):
    items = instr.split()
    for x in range(int(items[1])):
        stackDict[items[5]] += stackDict[items[3]][-1]
        stackDict[items[3]] = stackDict[items[3]][:-1]
 
outputStr = ''
for ind in range(1,10):
    outputStr += stackDict[str(ind)][-1]
    print(ind,outputStr)
    
print(stackDict)
print('Puzzle part 1 answer ', outputStr)


# Part 2
print(stackDict2)
for index, instr in enumerate(data[10::]):
    # print(instr)
    items = instr.split()
    stackDict2[items[5]] += stackDict2[items[3]][-int(items[1]):]
    stackDict2[items[3]] = stackDict2[items[3]][:-int(items[1])]
    # print(stackDict2)

print(stackDict2)
outputStr1 = ''
for ind in range(1,10):
    outputStr1 += stackDict2[str(ind)][-1]
    print(ind,outputStr1)
    
print(stackDict2)
print('Part 2 ', outputStr1)
