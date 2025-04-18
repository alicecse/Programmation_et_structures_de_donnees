class Tree:
    def __init__(self, label, *children):
        self._label = label
        self._children = children

    # label stocké au sein du nœud receveur. Ce dernier est une chaîne de caractères.
    def label(self) -> str : 
        return self._label   

    # tuple d'arbres, éventuellement vide.
    def children(self) -> tuple :
        return self._children
    
    def nb_children(self) -> int :
        return len(self._children) #retourne la longueur de la liste des children
    
    # récupère le i-ème sous-arbre
    def child(self, i: int) :
        return self._children[i]

    # True lorsque l'arbre est une feuille
    def is_leaf(self) :
        if len(self._children) == 0 : # pas de fils à l'arbre
            return True
        else :
            return False  
    
    # La profondeur d’un nœud correspond à la profondeur la plus élevée entre les fils à laquelle est ajouté 1. 
    # La profondeur d’une feuille est 0.
    def depth(self) -> int : 
        p_max = 0 
        if self.is_leaf() == False : 
            p_cur = 0
            for node in self._children : # on parcourt tous les fils du noeud
                p_cur = node.depth()
            if p_cur > p_max :
                p_max = p_cur
            p_max = p_max + 1
        return p_max     

    # renvoie une chaîne correspondant à la notation préfixée de l’arbre
    def __str__(self) -> str :
        if not self._label : 
            return f'pas d arbre défini' 
        elif self._label and len(self._children) == 0 :
            return self._label
        else :
            tree = f'{self._label}' + '('
            n = self.nb_children()
            for child in self._children : 
                tree += str(child)
                n = n-1
                if n != 0 :
                    tree += ','
                elif n == 0 :
                    tree += ')'
        return tree

    # compare deux arbres. renvoie True lorsque les deux arbres sont égaux, et False sinon
    def __eq__(self,other) -> bool : 
        if (not self._label and other._label) or (self._label and not other._label) :
            return False
        if self._label != other._label : 
            return False 
        if self.nb_children() != other.nb_children() :
            return False 
        for child1, child2 in zip(self.children(), other.children()): # zip() combine les deux listes en une seule liste
            if not child1.__eq__(child2):
                return False
        return True

    def eq_easier(self,other) -> bool :
        if str(self) == str(other) :
            return True
        return False
    
    def deriv(self, var: str):
        # Cas 1 : Feuille
        if self.is_leaf():
            if self.label() == var:
                return Tree('1')  # d(var)/d(var) = 1
            else:
                return Tree('0')  # d(const)/d(var) = 0

        # Cas 2 : Opérateur binaire
        op = self.label()
        left = self.child(0)
        right = self.child(1)

        if op == '+':
            # (u + v)' = u' + v'
            return Tree('+', left.deriv(var), right.deriv(var))

        elif op == '*':
            # (u * v)' = u' * v + u * v'
            u = left
            v = right
            u_der = u.deriv(var)
            v_der = v.deriv(var)
            return Tree('+',
                        Tree('*', u_der, v),
                        Tree('*', u, v_der))
        else:
            raise NotImplementedError(f"Opérateur '{op}' non supporté.")
    
        
if __name__ == '__main__':
    t1 = Tree('a')
    t2 = Tree('g',Tree('a'))
    t3 = Tree('f',Tree('a'),Tree('b'))
    t4 = Tree('')
    print(t3.nb_children())
    print(str(t1))
    print(str(t2))
    print(str(t3))
    print(str(t4))
    print(t1.__eq__(t2))
    print(t1.__eq__(t1))
    print(t1.eq_easier(t1))
    
    x_squared = Tree('*', Tree('X'), Tree('X'))
    term1 = Tree('*', Tree('3'), x_squared)
    term2 = Tree('*', Tree('5'), Tree('X'))
    term3 = Tree('7')
    poly = Tree('+', Tree('+', term1, term2), term3)
    d_poly = poly.deriv('X')
    print("Expression :", str(poly))
    print("Dérivée :", str(d_poly))


  