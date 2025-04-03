class Polynomial : 
    def __init__(self,coefficients) :
        self.coefs = coefficients
    
    def __str__(self) :
        pol = ''
        n = len(self.coefs)
        deg = n-1

        if n == 0 : # pas de coefs dans la liste
            return f'null'
        
        for i in range(n) :
            coef = self.coefs[i]
            current_degree = deg - i # degré du coef courant
            if coef != 0 :
                if current_degree == 0 : # 
                    pol += f'{coef}'
                elif current_degree == 1 : 
                    if coef == 1 :
                        pol += f'X'
                    elif coef != 1 :
                        pol += f'{coef}*X'
                else : 
                    if coef == 1 :
                        pol += f'X^{current_degree}'
                    elif coef != 1 :
                        pol += f'{coef}*X^{current_degree}'
                if  (i!=n-1 and any(self.coefs[j] != 0 for j in range(i+1, n))) or (i==n-2 and self.coefs[n-1]!=0): # Ajouter le signe '+' sauf pour le dernier terme ou si que des nuls après
                    pol += ' + '

        return pol
    
    def add(self,coefs_p2) :
        len_p1 = len(self.coefs)
        len_p2 = len(coefs_p2.coefs)
        M = max(len_p1,len_p2)
        m = min(len_p1,len_p2)

        liste_coef = [0]*M
        if len_p1 == len_p2 :
            for i in range(len_p1) :
                liste_coef[i] = self.coefs[i] + coefs_p2.coefs[i]
        else :
            for i in range(M-m) :
                if M == len_p1 :
                    liste_coef[i] = self.coefs[i]
                elif M == len_p2 :
                    liste_coef[i] = coefs_p2.coefs[i]
            for i in range(m) :
                if M == len_p1 :
                    liste_coef[i+m+1] = self.coefs[i+m+1] + coefs_p2.coefs[i]
                elif M == len_p2 :
                    liste_coef[i+m+1] = self.coefs[i] + coefs_p2.coefs[i+m+1]
        return Polynomial(liste_coef)

    def scalar(self, scal):
        return Polynomial([scal * coef for coef in self.coefs])

    def multiplication(self,coefs_p2) :
        liste_coefs=[0]*(len(self.coefs)+len(coefs_p2.coefs)-1) 
        for i1 in range(len(self.coefs)): # parcours des indices des coefs du polynôme n°1 
            for i2 in range(len(coefs_p2.coefs)): # parcours des indices des coefs du polynôme n°2 
                # multiplication des coefficients d'indices i1 et i2 
                liste_coefs[i1+i2] = liste_coefs[i1+i2] + self.coefs[i1]*coefs_p2.coefs[i2] 
    
        return Polynomial(liste_coefs)
    
if __name__ == '__main__':

    p1 = Polynomial([6, 1, 0, 1, 0])
    print('p1 =', str(p1))
    p1scal = p1.scalar(3)
    print('p1scal =', str(p1scal))
    p2 = Polynomial([6, 0, 1, 0, 1, 2])
    print('p2 =', str(p2))
    p3 = Polynomial([1, 0])
    print('p3 =', str(p3))
    p4 = Polynomial([1, 0, 0])
    print('p4 =', str(p4))
    padd = p1.add(p3)
    print('padd =', str(padd))
    pmul = p1.multiplication(p2)
    print('pmul =', str(pmul))



      
