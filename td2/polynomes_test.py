import unittest
from polynomes import Polynomial

class test_pol(unittest.TestCase):
    def test_polynome(self):
        p1 = Polynomial([6, 1, 0, 1, 0])
        print('p1 =', str(p1))
        assert(str(p1)=='6*X^4 + X^3 + X')

        p1scal = p1.scalar(3)
        print('p1scal =', str(p1scal))
        assert(str(p1scal)=='18*X^4 + 3*X^3 + 3*X')

        p2 = Polynomial([6, 0, 1, 0, 1, 2])
        pmul = p1.multiplication(p2)
        print('pmul =', str(pmul))
        assert(str(pmul)=='36*X^9 + 6*X^8 + 6*X^7 + 7*X^6 + 6*X^5 + 14*X^4 + 2*X^3 + X^2 + 2*X')

if __name__ == '__main__':
    unittest.main()
