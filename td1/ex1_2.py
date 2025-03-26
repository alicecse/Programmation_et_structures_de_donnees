#tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
tirage = ['z','y','g','o','m','a','t','i','q','u','e']
#mots_possibles = ['sacre', 'sabre', 'baser', 'cabre', 'garce', 'crase', 'brase', 'barge', 'caser', 'jaser', 'crabe', 'scare', 'aber', 'gare', 'sage', 'gars', 'rase', 'arec', 'acre', 'jars', 'case', 'base', 'cage', 'rage', 'jase', 'bras', 'race', 'ars', 'sac', 'arc', 'are', 'jar', 'jas', 'bar', 'bas', 'ace', 'cas', 'car', 'age', 'bac', 'cab', 'as', 'ra', 'sa', 'a']
#solution = sacre
#mots_possibles = ['abr','arbec','aajcsgbr','arbgescj']

# fonction qui prend la liste de mots
def liste() :
    liste = []
    f = open('frenchssaccent.dic','r')
    for ligne in f:
        liste.append(ligne[0:len(ligne)-1])
    f.close()
    #print(liste)
    #print(type(liste))
    return liste

mots_possibles = liste()
#print(type(mots_possibles))
#print(mots_possibles)

# fonction (tirage,mot), teste si on peut ecrire le mot, false sinon
def scrabble(tirage,mot) :
    tir = tirage.copy()
    c = 0
    for lettre in mot : 
        for i in tir : 
            if lettre == i :
                tir.remove(i)
                c = c + 1
                #print('remains',tirage)
    if len(mot) == c :
        return True
    return False
#print('can you write the word :',scrabble(tirage,'zygomatique'))
#print('can you write the word :',scrabble(tirage,'zygomaddtique'))

# fonction mot le plus long
def mot_le_plus_long(tirage,mots_possibles) :
    max = 0
    sol = None
    #print(mots_possibles)
    for mot in mots_possibles :
        numb_letters = 0
        if scrabble(tirage,mot) == True : 
            for j in mot :
                numb_letters = numb_letters + 1
                #print(numb_letters)
            if numb_letters > max :
                max = numb_letters
                sol = mot
                #print(sol)
    return sol

print('the longest word is :',mot_le_plus_long(tirage,mots_possibles))
