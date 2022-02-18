import copy

def echanger(a , b):
    return (b,a)

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

dic = {0 : [False, False, +1, +3],
       1 : [False, -1, +1, +3],
       2 : [False, -1, False, +3],
       3 : [-3, False, +1, +3],
       4 : [-3, -1, +1, +3],
       5 : [-3, -1, False, +3],
       6 : [-3, False, +1, False],
       7 : [-3, -1, +1, False],
       8 : [-3, -1, False, False]}

initial = [8,1,3,4,0,2,7,6,5]
vus = []

for i in range(20):
#while(calculateManhattan(initial) > 0):

    vus.append(copy.deepcopy(initial))
    afficherBien(initial)
    print()

    listePlateau = [initial, copy.deepcopy(initial), copy.deepcopy(initial), copy.deepcopy(initial), copy.deepcopy(initial)]

    for i in range(len(initial)):
        if initial[i] == 0:
            index = i

    liste = dic[index]
    #print(listePlateau)

    for i in range(1, 5):
        j = i-1
        if liste:
            #print(listePlateau[i], "     ", index)
            #print(listePlateau[i][index+(liste[j])])
            listePlateau[i][index],listePlateau[i][index+(liste[j])] = echanger(listePlateau[i][index], listePlateau[i][index+(liste[j])])
        else:
            listePlateau[i] = False



    min = 100
    for i in range(1,5):
        #print("min:", min, "listePlateau[i] : ", listePlateau[i])
        if (min > calculateManhattan(listePlateau[i]) and (listePlateau[i] not in vus) and listePlateau[i] != False):
            min = calculateManhattan(listePlateau[i])
            initial = listePlateau[i]
    #print("initial : ", initial)


    print("------------------------------")
    afficherBien(initial)
    print("Manhattan : ", calculateManhattan(initial))
    print("------------------------------")
