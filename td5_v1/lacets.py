from tkinter import Tk, Canvas, Button, Label
import random

# création fenêtre
root = Tk()
root.title('Canvas')
root.config(bg='grey')
root.geometry("700x500")
colors = ['black','blue','purple','pink','green']

# création canva
canvas = Canvas(root, width=650, height=450, bg='ivory')
canvas.pack()

# lecture mot dessinable 
def read_word(canvas, mot, h, w, y0, color):
    #color='black'
    x0=0
    (x, y) = (x0, y0)
    for lettre in mot:
        if lettre == 'H':
            canvas.create_line(x, y, x + h, y, fill=color, width=3)
            x += h
        elif lettre == 'U':
            canvas.create_line(x, y, x + w, y - h, fill=color, width=3)
            x += w
            y -= h
        elif lettre == 'D':
            canvas.create_line(x, y, x + w, y + h, fill=color, width=3)
            x += w
            y += h

# générer des mots dessinables à partir de croisements 
def generate_words(nb_fils, croisements):
    mots = ['' for i in range(nb_fils)]
    position_fils = {i: i for i in range(nb_fils)}  # {0: 0, 1: 1, 2: 2, 3: 3}...

    for chiffre in croisements:
        print(chiffre)
        for i in range(nb_fils):
            mots[i] += 'H'  # pour faire joli
        pos1 = chiffre       # numéro fil du haut croisement
        pos2 = chiffre + 1   # numéro fil du bas croisement

    # On cherche quel fil se trouve actuellement à la position pos1 (ligne du haut)
        for fil, position in position_fils.items():
            if position == pos1:
                fil1 = fil
                break
    # On cherche quel fil se trouve actuellement à la position pos2 (ligne du bas)
        for fil, position in position_fils.items():
            if position == pos2:
                fil2 = fil
                break

    # Le fil "en haut" descend, le fil "en bas" monte
        mots[fil1] += 'D'
        mots[fil2] += 'U'

    # Les autres fils continuent tout droit
        for f in range(nb_fils):
            if f != fil1 and f != fil2:
                mots[f] += 'H'

    # Échanger leurs positions dans le dictionnaire
        position_fils[fil1], position_fils[fil2] = position_fils[fil2], position_fils[fil1]

    # Fin : un dernier segment droit pour tous les fils
    for i in range(nb_fils):
        mots[i] += 'H'

    return mots

def ajouter_decorations():
    canvas.create_rectangle(5, 5, 645, 395, outline="gray")
    canvas.create_text(325, 20, text="Entrelacs Graphiques", font=("Arial", 14, "bold"), fill="darkblue")

# dessiner les entrelacs 
def dessiner_entrelacs(canvas, nb_fils, croisements, h, w):
    ajouter_decorations()
    mots = generate_words(nb_fils, croisements)
    y0 = 80
    pas = (nb_fils*w)%len(croisements)
    for j in range(nb_fils) : 
        lacet_j = read_word(canvas, mots[j], h, w, y0, colors[j])
        y0 += h + pas


def permuter_couleurs(canvas, nb_fils, croisements, h, w) :
    random.shuffle(colors)
    dessiner_entrelacs(canvas, nb_fils, croisements, h, w)

nb_fils = 4
croisements = [2, 1, 1, 0, 2]
(h,w)=(50,50)
bouton_quit = Button(root, text='Quitter', command=root.quit, bg='white')
bouton_quit.pack(side='left', padx=100, pady=10)
# lambda pour appel seulement quand on clique sur bouton
bouton_perm = Button(root, text="Permuter les couleurs", command=lambda:permuter_couleurs(canvas, nb_fils, croisements, h, w), bg='white')
bouton_perm.pack(side='right', padx=100, pady=10)

label_croisements = Label(root, text='Croisements :', bg='grey', fg='white', font=("Arial", 12),padx=1)
label_croisements.pack()

dessiner_entrelacs(canvas, nb_fils, croisements, h, w)
root.mainloop()

