import tkinter as tk
from tkinter import Tk, Canvas, Button, Label, Frame
from random import random
import numpy as np 

class Graphe:
    def __init__(self,graphe,width=700,height=700):
        self.graphe = graphe 

        # positions et vitesses initiales aléatoires
        self.position = np.array([(random()*width, random()*height) for i in range(len(graphe))])
        self.vit = np.array([((random()-0.5)*10, (random()-0.5)*10) for i in range(len(graphe))])

        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title('graphe')
        self.root.geometry('1000x1000')

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg='ivory')
        self.canvas.pack()

        self.k = 0.5 # raideur 
        self.time = 0.01 # néglige le temps
        self.repulsion = 300 # intensité des forces de répulsion
        self.amort = 0.9 # amortissement pour que s'arrête éventuellement (q4)
    
        self.root.bind('<Key>', self.on_canvas_click)
        self.draw()
        self.root.mainloop()

    def draw(self):
        self.canvas.delete('all')

        # arêtes
        for i in range(len(self.graphe)):
            for j in self.graphe[i]:  # sucs de i a j
                self.canvas.create_line(self.position[i][0], self.position[i][1], self.position[j][0], self.position[j][1],fill='purple',width=1)
        
        # sommets avec numéro
        for i,(x, y) in enumerate(self.position):
            self.canvas.create_oval(x-9,y-9,x+9,y+9,fill="#f3e1d4")
            self.canvas.create_text(x, y, text=str(i), fill='black', font=('Arial', 10, 'bold'))
    
    def on_canvas_click(self,event) :
        if event.char == 'f' :
            self.hooke()
            self.draw()

   
        # on calcule les nouvelles vitesses et positions des sommets :
        # - Force de ressorts (attraction entre sommets connectés)
        # - Force de répulsion électrique (entre tous les sommets)
        # - Amortissement
        # - Maintien dans la fenêtre
    def hooke(self) :
        forces_F = np.zeros_like(self.position) # array de 0 de même forme et type que nos positions

        # on calcule la force F des ressorts entre sommets voisins
        for i in range(len(self.graphe)) : # parcourt toutes les listes du graphe
            for j in self.graphe[i] :      # pour chaque sous-liste du graphe 
                if i == j : # pos i = (x_i,y_i), pos j = (x_j,y_j)
                    continue 
                else :
                    vecteur = self.position[j] - self.position[i]
                    norme_vecteur = np.linalg.norm(vecteur) # normalise le vecteur
                    force = (- self.k) * vecteur     # loi de hooke :  F=-k/delta l 
                    forces_F[i] += force
        
        # forces de répulsion
        for i in range(len(self.graphe)) :
            for j in range(len(self.graphe)) :
                if i == j:
                    continue
                else :
                    vect_repulsio = self.position[i] - self.position[j]
                    norme_rep = np.linalg.norm(vect_repulsio)  + 1e-6   # le 1e-6 évite la division par 0
                    repulsion = self.repulsion / norme_rep**2                 # force = q/r^2
                    forces_F[i] += repulsion * (vect_repulsio / norme_rep)

                    # je pense avoir fais une erreur ici, car si j'appuie sur 'f' jusqu'à l'arrêt des particules,
                    # certaines se stabilisent sur la même position, ce qui devrait être impossible avec la répulsion

        # loi de newton et màj vitesse et position
        for i in range(len(self.graphe)):
            self.vit[i] = self.amort * (self.vit[i] + self.time*forces_F[i]) 
            # F=ma avec m = 1 et amortissement pour qu'elles s'arrêtent éventuellement
            self.position[i] += self.vit[i] # d=v*t temps négligé

            # Garder dans la fenêtre
            x, y = self.position[i]
            x = min(max(x, 10), self.width - 10)
            y = min(max(y, 10), self.height - 10)
            self.position[i] = np.array([x, y])  
            
graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], 
[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]

if __name__ == "__main__":
    Graphe(graph)
    
