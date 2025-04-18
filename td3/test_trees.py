import unittest
from trees import Tree


class TestTree(unittest.TestCase):
    def test_tree(self):
        
        t2 = Tree('a')
        t3 = Tree('b')
        t1 = Tree('f',t2,t3) # permet de mettre même adresse pour t2 et Tree('a') 

        self.assertEqual(t1.label(), 'f')
        self.assertEqual(t1.child(0),t2)
        self.assertFalse(t1.is_leaf())
        self.assertEqual(t1.nb_children(), 2)
        self.assertEqual(t2.nb_children(), 0)
        self.assertTrue(t3.is_leaf())
        self.assertEqual(t1.depth(),1)
        self.assertEqual(t2.depth(),0)
    
    # chaînes a, g(a) et f(a,b)
    def test_str(self) :
        t1 = Tree('a')
        t2 = Tree('g',Tree('a'))
        t3 = Tree('f',Tree('a'),Tree('b'))
        self.assertEqual(str(t1),'a')
        self.assertEqual(str(t2),'g(a)')
        self.assertEqual(str(t3),'f(a,b)')
        self.assertNotEqual(str(t3),'g(a,b)')
    
    def test_eq(self):
        t1 = Tree('a')
        t2 = Tree('g',Tree('a'))
        self.assertFalse(t1.__eq__(t2))
        self.assertTrue(t1.__eq__(t1))
        self.assertTrue(t1.eq_easier(t1))


if __name__ == '__main__':
    unittest.main()
  
  