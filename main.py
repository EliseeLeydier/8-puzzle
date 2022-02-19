from queue import PriorityQueue
import copy

def enfantsF(plateau):
    print("sortir")
    dic = {0 : [False, False, +1, +3],
        1 : [False, -1, +1, +3],
        2 : [False, -1, False, +3],
        3 : [-3, False, +1, +3],
        4 : [-3, -1, +1, +3],
        5 : [-3, -1, False, +3],
        6 : [-3, False, +1, False],
        7 : [-3, -1, +1, False],
        8 : [-3, -1, False, False]}

    for i in range(len(plateau)):
            if plateau[i] == 0:
                index = i

    listeEnfants = []
    for i in range(1, 5):
        j = i-1
        if dic[index]:
            plateau2 = copy.deepcopy(plateau)
            plateau2[index],plateau2[index+(dic[index][j])] = plateau2[index+(dic[index][j])],plateau2[index]
        listeEnfants.append(plateau2)
    return listeEnfants



class etat:

    def __init__ (self, initial, profondeur ):
        self.initial = initial
        self.profondeur = profondeur
        self.goal = [0,1,2,3,4,5,6,7,8]
    
    def calculateManhattan(self, plateau):
        manDict = 0
        for i,item in enumerate(plateau):
            prev_row,prev_col = int(i/ 3) , i % 3
            goal_row,goal_col = int((item /3)),(item % 3)
            if plateau[i] != 0:
                manDict += abs(prev_row-goal_row) + abs(prev_col - goal_col)
        return manDict

    def afficher(self):
        
        for i in range(len(self.initial)):
            if i%3 == 0 and i != 0:
                print('|')
            print('|', self.initial[i], end = "")
        print('|')
    
    def estResolu(self):
        return self.initial == self.goal

    def enfants(self, plateau):
        print("sortir")
        dic = {0 : [False, False, +1, +3],
            1 : [False, -1, +1, +3],
            2 : [False, -1, False, +3],
            3 : [-3, False, +1, +3],
            4 : [-3, -1, +1, +3],
            5 : [-3, -1, False, +3],
            6 : [-3, False, +1, False],
            7 : [-3, -1, +1, False],
            8 : [-3, -1, False, False]}

        for i in range(len(plateau)):
                if plateau[i] == 0:
                    index = i

        listeEnfants = []
        for i in range(1, 5):
            j = i-1
            if dic[index]:
                plateau2 = copy.deepcopy(plateau)
                plateau2[index],plateau2[index+(dic[index][j])] = plateau2[index+(dic[index][j])],plateau2[index]
            listeEnfants.append(plateau2)
        return listeEnfants

    def A(self):
        vus = []
        queue = PriorityQueue()
        manhattan = self.calculateManhattan(self.initial)
        queue.put((manhattan, self.initial))

        while not queue.empty():
            neud = queue.get()[1]
            vus.append(neud)

            if (self.estResolu()):
                return(neud)
                

            print(enfantsF(neud))
            listeEnfant = self.enfants(neud)
            print(neud)
            for enfant in listeEnfant:
                print(enfant)
                if enfant not in vus:
                    manhattan = self.calculateManhattan(enfant)
                    queue.put((manhattan, self.initial))



plateauDepart = etat([8, 1, 3, 4, 0, 2, 7, 6, 5], 0)
#print(plateauDepart.calculateManhattan())
print(type(plateauDepart.initial))
plateauDepart.afficher()
plateauDepart.A()
