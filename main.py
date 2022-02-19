import copy

#Fonction qui cherche la distance minimum de manathan et qui renvoie la liste associé a cette disctance
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
        self.goal = [0,1,2,3,4,5,6,7,8]
    
    #Programe qui calcule la distance de Manhattan
    def calculateManhattan(self, plateau):
        manDict = 0
        for i,item in enumerate(plateau):
            prev_row,prev_col = int(i/ 3) , i % 3
            goal_row,goal_col = int((item /3)),(item % 3)
            if plateau[i] != 0:
                manDict += abs(prev_row-goal_row) + abs(prev_col - goal_col)
        return manDict

    #Fonction qui afficher corectement le plateau
    def afficher(self, plateau):
        
        for i in range(len(plateau)):
            if i%3 == 0 and i != 0:
                print('|')
            print('|', plateau[i], end = "")
        print('|')
    
    #Fonction qui vérifie si on a réussis a résolver les puzzle
    def estResolu(self):
        return self.initial == self.goal

    #Fonction qui génère tous les enfants d'une liste
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

        # On cherche la tuile vide dans le plateau parent
        for i in range(len(plateau)):
                if plateau[i] == 0:
                    index = i

        listeEnfants = []
        #En fonction de ou est la tuile vide sur le plateau, on bouge la tuile vide a gauche, droite, en haut et en bas (si possible)
        for i in range(1, 5):
            j = i-1
            if dic[index]:
                plateau2 = copy.deepcopy(plateau)
                plateau2[index],plateau2[index+(dic[index][j])] = plateau2[index+(dic[index][j])],plateau2[index]
            listeEnfants.append(plateau2)
        return listeEnfants

    #fonction de l'algorithme A*
    def A(self):
        vus = [] # Pour ranger las plateau déja vu (et pas refaire la meme chose)
        compteur = 0 #Pas utiles pour le truc final 
        manhattan = self.calculateManhattan(self.initial)
        queue = [] 
        queue.append((manhattan, self.initial))
        #print("manathan")

        while True:

            #if pas utiles pour le truc final 
            if compteur > 20:
                return


            #print(queue)
            neud = minim(queue) #On met la liste avec le moins de distance de manathan
            print(neud)
            neud = neud[1] 
            vus.append(neud) # et on rajoute la liste dans les liste déja visité
            #self.afficher(neud)
            print()

            # Si c'est résolu, ca s'arrette
            if (self.estResolu()):
                return(neud)
                
            
            listeEnfant = self.enfants(neud)
            
            queue = []
            #parcours la liste des enfants et les rajoute dans queue
            for enfant in listeEnfant:
                #print(enfant)
                if enfant not in vus:
                    compteur += 1
                    manhattan = self.calculateManhattan(enfant)
                    queue.append((manhattan, enfant))



plateauDepart = etat([1,8,2,0,4,3,7,6,5], 0) # plateau de départ
#print(plateauDepart.calculateManhattan())
print(type(plateauDepart.initial))
plateauDepart.A()
