import matplotlib.pyplot as plt

### Exerice 1 ###

'''
Pour définir la classe Hashtable : 

Méthodes nécessaires (ce que la table sait faire) : 
- init : initialise les attributs
- put : insère nouveeau tuple ou met à jour la valeur si la clé existe déjà
- get : recherche la valeur associée à une clé donnée
il faut des fonctions pour manipuler les listes stockées dans chaque case :
par exemple pour ajouter un tuple, enlever un tuple, vérifier si un tuple appartient à la case ...

Attributs nécessaires (ce que la table contient) : 
- taille N de la table (nombre total de cases) 
- tableau principal = liste de listes 
- fonction de hashage pour transformer une clé en index dans la table
- répartition : affiche la taille des listes de collision en fonction de l’index du tableau principal (0..N-1)
'''

### Exercices 2, 3, 4, 5 ###

def hash_naif(string) -> int : 
    h = 0 
    if string == '' :
        return f'empty string'
    for i in string : 
        h = h + ord(i)
    return h 

def hash_better_rep(string) -> int :
    h = 0 
    for char in string :
        h = 31 * h + ord(char)
    return h & 0xFFFFFFFF  

# fonction qui prend la liste de mots
def liste() :
    liste = []
    f = open('frenchssaccent.dic','r')
    for ligne in f:
        liste.append(ligne[0:len(ligne)-1])
    f.close()
    return liste

class Hashtable:
    def __init__(self, hash_function, N):
        self.size = N  # Taille N de la table 
        self.table=[[] for i in range(N)] # Table principale avec des listes vides
        self.hash_function = hash_function  # Fonction de hachage passée en argument

    def put(self, key, value):
        h_key = self.hash_function(key)
        index = h_key % self.size
        for couple in self.table[index]:
            if couple[0] == key:
                couple[1] = value  # Met à jour la valeur si la clé existe déjà
                return self.table
        self.table[index].append([key, value])  # Insère un nouveau tuple clé-valeur si clé existe pas déjà

    def put_resize(self, key, value):
        h_key = self.hash_function(key)
        index = h_key % self.size

        for couple in self.table[index]:
            if couple[0] == key:
                couple[1] = value  # Met à jour la valeur si la clé existe déjà
                return self.table
        self.table[index].append([key, value])

        if len(self.table) > 1.2 * self.size:
            self.resize()  # Insère un nouveau tuple clé-valeur si clé existe pas déjà

    def resize(self):
        self.size = 2*self.size  # double la taille de la table
        new_table = [[] for i in range(self.size)]

        # réinsérer tous les éléments dans la nouvelle table
        for element in self.table:
            for (key, value) in element:
                hash_key = self.hash_naif(key)
                index = hash_key % self.size
                new_table[index].append([key, value])
        self.table = new_table

    def get(self, key):
        index = self.hash_function(key) % self.size
        for couple in self.table[index]:
            if couple[0] == key:
                return couple[1]  # Renvoie la valeur associée à la clé
        return f'aucun tuple n est associé à cette clé' 
    
    def repartition(self):
        size_collision = [len(liste) for liste in self.table]
        return size_collision  
    
    def hash_dico(self) :
        mots = liste()
        for mot in mots :
            self.put(mot, len(mot))
        print('répartiton', self.repartition())
    
    def hash_dico_resize(self) :
        mots = liste()
        for mot in mots :
            self.put_resize(mot, len(mot))
        print('répartiton', self.repartition())

    def afficher_repartition(self, titre):
        repartition = self.repartition()
        x = range(len(repartition))
        y = repartition
        plt.bar(x, y, width=1.0, color='blue')
        plt.title(titre)
        plt.xlabel('Index de la table')
        plt.ylabel("Nombre d’éléments")
        plt.show()

if __name__ == "__main__":
    hsht = Hashtable(hash_naif,5)
    hs_resize = Hashtable(hash_naif,300)

    print('s1 :',hash_naif('abc'))
    print('s2 :',hash_naif(''))

    hsht.put('abc',3)
    print('test1 :',hsht.get('aaa')) # aucun tuple
    print('test2 :',hsht.get('abc')) # 3
    print('size1',hsht.repartition())
    
    hsht.put('abc',47)
    print('test3 :',hsht.get('abc')) # 47
    
    hsht.put('cab',7)
    print('test4 :',hsht.get('cab')) # 7
    print('test5 :',hsht.get('coucou')) # aucun
    hsht.put('aco',1)
    hsht.put('bili',18)
    print('test4 :',hsht.repartition()) 

    ht_dico_320 = Hashtable(hash_naif, 320)
    ht_dico_320.hash_dico()
    ht_dico_320.afficher_repartition('rep 320')
    ht_dico_1000 = Hashtable(hash_naif, 1000)
    ht_dico_1000.hash_dico()
    ht_dico_1000.afficher_repartition('rep 1000')

    h_better_320 = Hashtable(hash_better_rep,320)
    h_better_320.hash_dico()
    h_better_320.afficher_repartition('rep 320')
    h_better_1000 = Hashtable(hash_better_rep,1000)
    h_better_1000.hash_dico()
    h_better_1000.afficher_repartition('rep 1000')

    h_better_320.hash_dico_resize()
    h_better_320.afficher_repartition('rep 320 resize')

y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
N = len(y)
x = range(N)
width = 1/1.5
plt.bar(x, y, width, color="blue")
# plt.show()    
