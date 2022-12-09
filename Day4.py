# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:44:18 2022

@author: straybj
"""

import numpy as np

data = np.loadtxt('Inputs/inputDay4.txt',dtype=str,delimiter=',')


with open("Inputs/inputDay4.txt") as f:
    data = f.readlines()
    data  = [d.replace('-',',') for d in data]
    data = np.loadtxt(data,delimiter=',')


# puzInput = [d.replace('\n','') for d in data]
# puzInput = [d.replace('-',',') for d in puzInput]

# count = 0
# for i,v in enumerate(data):
#     if (v[0]>=v[2]) and (v[1]<=v[3]):
#         count +=1
#         print(i, v)
#     elif (v[2]>=v[0]) and (v[3]<=v[1]):
#         count +=1
#         print(i, v)
#     else:
#         pass

# print('Count: ',count)


# part 2
count2 = 0
for i,v in enumerate(data):
    if (v[3]>=v[0]) and (v[1]>=v[3]):
        count2 +=1
        print('hi',i, v)
    elif (v[1]>=v[2]) and (v[3]>=v[1]):
        count2 +=1
        print('bye',i, v)
    else:
        pass

print('Count: ',count2)

