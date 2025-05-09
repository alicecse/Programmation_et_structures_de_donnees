from tkinter import Tk, Canvas, Button, Label, Frame
import random

class Data:
    def __init__(self, nb_fils, croisements):
        self.nb_fils = nb_fils
        self.croisements = croisements
        self.neutralised = set()  # Indices des croisements déjà dénoué

    def read_word(self, canvas, mot, h, w, y0, color):
        # Trace une ligne en suivant le mot donné (H, U, D)
        x, y = 0, y0
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

    def generate_words(self):
        mots = ['' for i in range(self.nb_fils)]
        position_fils = {i: i for i in range(self.nb_fils)}
        for index, chiffre in enumerate(self.croisements):
            for i in range(self.nb_fils):
                mots[i] += 'H'
            if index in self.neutralised:
                continue  # Ignore les croisements neutralisés
            pos1, pos2 = chiffre, chiffre + 1
            fil1 = fil2 = None
            for fil, pos in position_fils.items():
                if pos == pos1:
                    fil1 = fil
                elif pos == pos2:
                    fil2 = fil
            if fil1 is not None and fil2 is not None:
                mots[fil1] += 'D'
                mots[fil2] += 'U'
                for f in range(self.nb_fils):
                    if f != fil1 and f != fil2:
                        mots[f] += 'H'
                # On échange les positions
                position_fils[fil1], position_fils[fil2] = position_fils[fil2], position_fils[fil1]
        for i in range(self.nb_fils):
            mots[i] += 'H'
        return mots

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title('Canvas')
        self.root.config(bg='grey')
        self.root.geometry('1200x650')

        self.canvas = Canvas(self.root, width=650, height=400, bg='ivory')
        self.canvas.pack()

        (self.h, self.w) = (50, 50)
        self.colors = ['black', 'blue', 'purple', 'pink', 'green', 'magenta', 'cyan']

        self.nb_fils = 7
        self.croisements = [4, 1, 1, 3, 2, 5, 4]
        self.dat = Data(self.nb_fils, self.croisements)

        self.canvas.bind('<Button-1>', self.on_canvas_click)

    def ajouter_decorations(self):
        # Dessine le cadre et le titre dans le canvas
        width = int(self.canvas.cget('width'))
        height = int(self.canvas.cget('height'))
        self.canvas.create_rectangle(5, 5, width - 5, height - 5, outline='gray')
        self.canvas.create_text(width // 2, 20, text='Entrelacs Graphiques', font=('Arial', 14, 'bold'), fill='darkblue')

    def dessiner_entrelacs(self):
        # Redimensionne le canvas en fonction du contenu
        largeur = (len(self.croisements) + 2) * self.w
        hauteur = (self.nb_fils + 1) * (self.h + 10)

        self.canvas.config(width=largeur, height=hauteur)
        self.canvas.delete('all')
        self.ajouter_decorations()

        mots = self.dat.generate_words()
        y0 = 80
        pas = 10  # Espace vertical entre les fils
        for j in range(self.nb_fils):
            self.dat.read_word(self.canvas, mots[j], self.h, self.w, y0, self.colors[j % len(self.colors)])
            y0 += self.h + pas

    def permuter_couleurs(self):
        random.shuffle(self.colors)
        self.dessiner_entrelacs()

    def rand_entrelac(self, max_fils, max_crois):
        self.nb_fils = random.randint(2, max_fils)
        nb_crois = random.randint(1, max_crois)
        self.croisements = [random.randint(0, self.nb_fils - 2) for i in range(nb_crois)]
        self.dat = Data(self.nb_fils, self.croisements)
        self.dat_neutralised = set()
        self.dessiner_entrelacs()

    def get_all_reidemeister_pairs(self, croisements):
        # Renvoie toutes les paires (i,j) valides pour noeuds de reidemeister
        paires = []
        for i in range(len(croisements)):
            for j in range(i + 1, len(croisements)):
                if croisements[i] == croisements[j]:
                    fils_concernes = [croisements[i], croisements[i] + 1]
                    entre = croisements[i + 1:j]
                    if all(c not in fils_concernes and c != croisements[i] - 1 and c != croisements[i] + 1 for c in entre):
                        paires.append((i, j))
        return paires

    def on_canvas_click(self, event):
        # Gère le clic sur le canvas pour dénouer un croisement
        x_click, y_click = event.x, event.y
        toutes_les_paires = self.get_all_reidemeister_pairs(self.croisements)
        if not toutes_les_paires:
            return

        x = self.h
        croisement_positions = []
        for c in self.croisements:
            croisement_positions.append(x)
            x += self.w

        # Vérifie si clic proche d'une des paires
        for i, j in toutes_les_paires:
            if ((i < len(croisement_positions) and abs(x_click - croisement_positions[i]) < self.w // 2) or
                (j < len(croisement_positions) and abs(x_click - croisement_positions[j]) < self.w // 2)):
                self.dat.neutralised.add(i)
                self.dat.neutralised.add(j)
                self.dessiner_entrelacs()
                break  

    def run_forever(self):
        self.dat_neutralised = set()
        self.dat.neutralised = self.dat_neutralised
        self.dessiner_entrelacs()

        Button(self.root, text='Random Entrelac', command=lambda: self.rand_entrelac(15, 15), bg='white').pack(side='right', padx=150, pady=10)
        Button(self.root, text='Quitter', command=self.root.quit, bg='white').pack(side='left', padx=100, pady=10)
        Button(self.root, text="Permuter les couleurs", command=self.permuter_couleurs, bg='white').pack(side='right', padx=100, pady=10)

        label_croisements = Label(self.root, text=f'Croisements : {self.croisements}', bg='grey', fg='white', font=('Arial', 11), width=1000, anchor='w')
        label_croisements.pack(side='top', fill='x', padx=5, pady=5)

        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run_forever()
