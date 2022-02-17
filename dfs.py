import copy

from pygame import init

def calculateManhattan(initial):
    initial_config = initial
    manDict = 0
    #print(list(enumerate(initial_config)))
    for i,item in enumerate(initial_config):
        #print(i, item)
        prev_row,prev_col = int(i/ 3) , i % 3
        goal_row,goal_col = int((item /3)),(item % 3)
        #print("prev row : ", prev_row, ", col : ", prev_col)
        #print("goal row : ", goal_row, ", col : ", goal_col)
        #print()
        manDict += abs(prev_row-goal_row) + abs(prev_col - goal_col)
    return manDict

def afficherBien(liste):
    
    for i in range(len(liste)):
        if i%3 == 0 and i != 0:
            print('|')
        print('|', liste[i], end = "")
    print('|')

initial = [8,1,3,4,0,2,7,6,5]

for i in range(15):
#while(calculateManhattan(initial) > 0):

    afficherBien(initial)
    print()

    listePlateau = [initial, copy.deepcopy(initial), copy.deepcopy(initial), copy.deepcopy(initial), copy.deepcopy(initial)]

    for i in range(len(initial)):
        if initial[i] == 0:
            index = i

    liste = [-3, -1, +1, +3]

    for i in range(1, 5):
        j = i-1
        #print(listePlateau[i])
        listePlateau[i][index],listePlateau[i][index+(liste[j])] = listePlateau[i][index+(liste[j])],listePlateau[i][index]
        #print(listePlateau[i])
        #print()

    # print("--1--")
    # print(listePlateau[0])
    # print("--2--")
    # print(listePlateau[1])
    # print("--3--")
    # print(listePlateau[2])
    # print("--4--")
    # print(listePlateau[3])
    # print("--5--")
    # print(listePlateau[4])


    #print(calculateManhattan(listePlateau[0]))
    #print(calculateManhattan(listePlateau[1]))
    #print(calculateManhattan(listePlateau[2]))
    #print(calculateManhattan(listePlateau[3]))
    #print(calculateManhattan(listePlateau[4]))

    min = listePlateau[1]
    for i in range(2,5):
        if (min > listePlateau[i]):
            min = listePlateau[i]
    initial = min