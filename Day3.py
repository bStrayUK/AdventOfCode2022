import numpy as np

with open("Inputs/inputDay3.txt") as f:
    data = np.array(f.readlines())
    
# data = np.array(['vJrwpWtwJgWrhcsFMMfFFhFp','jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg',
# 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw'])
# Could use .find(letter) which either returns index or -1 if not in there. 


totalPoints = 0

for i,line in enumerate(data):
    
    lenLine = len(line)//2   
    letterFound = 0
    while letterFound == False:
        for j,letter in enumerate(line[0:lenLine]):
            guessLetter = line[lenLine:].find(letter)
            if guessLetter != -1:
                if letter.islower():
                    totalPoints += ord(letter) - 96
                else:
                    totalPoints += ord(letter) - 38
                letterFound = 1
                break
            
    print(line[0:lenLine],line[lenLine:],letter,guessLetter, totalPoints)
print('Total points ', totalPoints)
        

# Part 2
totalPoints2 = 0

for i,line in enumerate(data):
    if i%3 == 0:
        letterFound = 0 
        while letterFound == False:
            for j,letter in enumerate(line):
                guessBadge1 = data[i+1].find(letter)
                guessBadge2 = data[i+2].find(letter)
                if (guessBadge1 !=-1) and (guessBadge2 !=-1):
                    if letter.islower():
                        totalPoints2 += ord(letter) - 96
                    else:
                        totalPoints2 += ord(letter) - 38
                    letterFound = 1
                    break
        print(letter,data[i+1][guessBadge1],data[i+2][guessBadge2], totalPoints2)
print('Total points 2 ', totalPoints2)             