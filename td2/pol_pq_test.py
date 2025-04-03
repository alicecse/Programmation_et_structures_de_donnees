import unittest
from pol_pq import Polynomial

class test_pol(unittest.TestCase):
    def test_polynome(self):
        p1 = Polynomial([6, 6, 0, 6, 0],7,10)
        assert(str(p1)=='6*X^4 + 6*X^3 + 6*X')

        p2 = Polynomial([6, 0, 1, 0, 1, 2],7,10)
        assert(str(p2)=='6*X^5 + X^3 + X + 2')
    
        p3 = Polynomial([1, 0],7,10)
        assert(str(p3)=='X')

        p4 = Polynomial([1, 0, 0],7,10)
        assert(str(p4)=='X^2')

        padd = p1.add(p3)
        assert(str(padd)=='6*X^4 + 6*X^3')

        pmul = p1.multiplication(p2)
        assert(str(pmul)=='X^9 + X^8 + 6*X^7 + 6*X^5 + 3*X^4 + 5*X^3 + 6*X^2 + 5*X')

        p1_rescale = p1.rescale(4)
        assert(str(p1_rescale)=='2*X^4 + 2*X^3 + 2*X')
 

if __name__ == '__main__':
    unittest.main()
