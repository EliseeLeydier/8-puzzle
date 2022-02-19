import copy

def minim(listeEtat):
    minimum = listeEtat[0][0]
    indexe = 0
    for i in range(len(listeEtat)):
        manath = listeEtat[i][0]
        plateau = listeEtat[i][1]
        if (minimum > manath):
            minimum = manath
            indexe = 1
    return listeEtat[indexe]

class etat:

    def __init__ (self, initial, profondeur ):
        self.initial = initial
        self.profondeur = profondeur
        self.goal = [1,2,3,4,5,6,7,8,0]
    
    def calculateManhattan(self, plateau):
        manDict = 0
        for i,item in enumerate(plateau):
            prev_row,prev_col = int(i/ 3) , i % 3
            goal_row,goal_col = int((item /3)),(item % 3)
            if plateau[i] != 0:
                manDict += abs(prev_row-goal_row) + abs(prev_col - goal_col)
        return manDict

    def afficher(self, plateau):
        
        for i in range(len(plateau)):
            if i%3 == 0 and i != 0:
                print('|')
            print('|', plateau[i], end = "")
        print('|')
    
    def estResolu(self):
        return self.initial == self.goal

    def enfants(self, plateau):
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
        compteur = 0
        manhattan = self.calculateManhattan(self.initial)
        queue = []
        queue.append((manhattan, self.initial))
        #print("manathan")

        while True:


            if compteur > 10:
                return
            #print(queue)
            neud = minim(queue)
            print(neud)
            neud = neud[1]
            vus.append(neud)
            #self.afficher(neud)
            print()

            if (self.estResolu()):
                return(neud)
                
            listeEnfant = self.enfants(neud)
            
            queue = []
            for enfant in listeEnfant:
                #print(enfant)
                if enfant not in vus:
                    compteur += 1
                    manhattan = self.calculateManhattan(enfant)
                    queue.append((manhattan, enfant))



plateauDepart = etat([1,8,2,0,4,3,7,6,5], 0)
#print(plateauDepart.calculateManhattan())
print(type(plateauDepart.initial))
plateauDepart.A()


def AStar_search(given_state , n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    evaluation = root.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
    frontier.put((evaluation[1], counter, root)) #based on A* evaluation

    while not frontier.empty():
        current_node = frontier.get()
        print()
        print(current_node[2].state)
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            print(child.state)
            if child.state not in explored:
                counter += 1
                evaluation = child.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
                frontier.put((evaluation[1], counter, child)) #based on A* evaluation
    return
