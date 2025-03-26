# on ajoute le joker au dictionnaire,
# et on change la fonction scrabble pour autoriser une utilisation du joker

tirage = ['z','y','g','o','m','t','i','q','u','e','?']

# fonction qui prend la liste de mots
def liste() :
    liste = []
    f = open('frenchssaccent.dic','r')
    for ligne in f:
        liste.append(ligne[0:len(ligne)-1])
    f.close()
    return liste

mots_possibles = liste()

dict = {
  'a' : 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1,'o': 1,'r': 1,'s': 1,'t': 1,'u': 1,
  'd' : 2,'g' : 2,'m' : 2,
  'b':3,'c':3,'p':3,
  'f':4,'h':4,'v':4,
  'j':8,'q':8,
  'k':10,'w':10,'x':10,'y':10,'z':10,
  '?':0}

def score(mot) : 
    c = 0
    for lettre in mot : 
        c = c + dict[lettre]
    return c 

# fonction (tirage,mot), teste si on peut ecrire le mot, false sinon
def scrabble(tirage,mot) :
    tir = tirage.copy()
    joker_utile = False
    c = 0
    for lettre in mot : 
        if lettre in tir : 
            for i in tir : 
                if lettre == i :
                    tir.remove(i)
                    c = c + 1
        elif '?' in tir and joker_utile != True : 
            tir.remove('?')
            c = c + 1
            joker_utile = True
    if len(mot) == c :
        return True
    return False
#print('can you write the word :',scrabble(tirage,'zygomatiquee'))
#print('can you write the word :',scrabble(tirage,'zygomatique'))

# fonction mot le plus long
def max_score(tirage,mots_possibles) :
    max = 0
    sol = None
    for mot in mots_possibles :
        if scrabble(tirage,mot) == True : 
            sc = score(mot)
            if sc > max :
                max = sc
                sol = mot
    return (sol,max)

print('the longest word is :',max_score(tirage,mots_possibles))
