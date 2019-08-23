import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(0,2)
        self.assertEqual("0", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        # denominator = 0 should be shown
        f = Fraction(0,0)
        self.assertEqual('0/0', f.__str__())
        f = Fraction(1,0)
        self.assertEqual('1/0', f.__str__())
        f = Fraction(1,-0)
        self.assertEqual('1/0', f.__str__())
        f = Fraction(-5,0)
        self.assertEqual('-1/0', f.__str__())
        f = Fraction(-2,-0)
        self.assertEqual('-1/0', f.__str__())

    def test_init(self):
        #Test not int
        with self.assertRaises(TypeError):
            f = Fraction('dasg','dsag')
        with self.assertRaises(TypeError):
            f = Fraction('1',0)
        with self.assertRaises(TypeError):
            f = Fraction(3,'sdag')
        f = Fraction(1,2)
        self.assertEqual(1, f.numerator)
        self.assertEqual(2, f.denominator)
        f = Fraction(2,-3)
        self.assertEqual(-2, f.numerator)
        self.assertEqual(3, f.denominator)
        f = Fraction(-3,5)
        self.assertEqual(-3, f.numerator)
        self.assertEqual(5, f.denominator)
        f = Fraction(-2,-3)
        self.assertEqual(2, f.numerator)
        self.assertEqual(3, f.denominator)
        f = Fraction(0,0)
        self.assertEqual(0, f.numerator)
        self.assertEqual(0, f.denominator)
        f = Fraction(1,0)
        self.assertEqual(1, f.numerator)
        self.assertEqual(0 ,f.denominator)
        f = Fraction(0,-1)
        self.assertEqual(0, f.numerator)
        self.assertEqual(1, f.denominator)
        f = Fraction(0,2)
        self.assertEqual(0, f.numerator)
        self.assertEqual(1, f.denominator)


        

    # TODO Write tests for __init__, __eq__, +, *.
    # Here is an example, but you must add more test cases.  
    # The test requires that your __eq__ is correct.
    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12) + Fraction(2,3))
        self.assertEqual(Fraction(2), Fraction(3,2) + Fraction(1,2))
        self.assertEqual(Fraction(3,2), Fraction(5,4) + Fraction(1,4))
        self.assertEqual(Fraction(-5,9), Fraction(-1,9) + Fraction(-4,9))
        self.assertEqual(Fraction(0,0), Fraction(1,0) + Fraction(2,0))
        self.assertEqual(Fraction(0,0), Fraction(1,0) + Fraction(-4,0))
        self.assertEqual(Fraction(0,0), Fraction(100,0) + Fraction(9))

    def test_subtract(self):
        self.assertEqual(Fraction(1,2), Fraction(1) - Fraction(1,2))
        self.assertEqual(Fraction(3,4), Fraction(4,4) - Fraction(1,4))
        self.assertEqual(Fraction(1), Fraction(999999) - Fraction(999998))
        self.assertEqual(Fraction(-5,10), Fraction(-1) - Fraction(1,-2))
        self.assertEqual(Fraction(0), Fraction(1) - Fraction(1) )
        self.assertEqual(Fraction(0,0), Fraction(0,0) - Fraction(0,0))
        self.assertEqual(Fraction(24,30), Fraction(1)-Fraction(1,5))


    def test_multiply(self):
        self.assertEqual(Fraction(3,4), Fraction(1) * Fraction(3,4))
        self.assertEqual(Fraction(2), Fraction(1) * Fraction(2))
        self.assertEqual(Fraction(5,6), Fraction(5,6) * Fraction(2,2))
        self.assertEqual(Fraction(4,8), Fraction(1,2) * Fraction(4,4))
        self.assertEqual(Fraction(5,5), Fraction(1) * Fraction(1))
        self.assertEqual(Fraction(0,0), Fraction(0,0) * Fraction(9))
        self.assertEqual(Fraction(99,0), Fraction(1,0) * Fraction(99))
        self.assertEqual(Fraction(-1), Fraction(2,2) * Fraction(-1))

    def test_negation(self):
        f = Fraction(2,2)
        -f #negating
        self.assertEqual(Fraction(-1),f)
        f = Fraction(2,0)
        -f
        self.assertEqual(Fraction(-2,0),f)
        f = Fraction(4,-5)
        -f
        self.assertEqual(Fraction(4,5),f)
        f = Fraction(0,0)
        -f 
        self.assertEqual(Fraction(0,0),f)
        f = Fraction(2,0)
        -f 
        self.assertEqual(Fraction(-2,0),f)


    
    def test_greater(self):
        self.assertTrue(Fraction(1,2)>Fraction(1,3))
        self.assertTrue(Fraction(2,0)>Fraction(0,0))
        self.assertTrue(Fraction(999999,8)>Fraction(88888,7))
        self.assertFalse(Fraction(0,0)>Fraction(1,0))
        self.assertTrue(Fraction(0,0)>Fraction(-1,0))
        self.assertFalse(Fraction(0,0)>Fraction(0,0))
        

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        
        #TODO write more tests using other cases.
        # Consider special values like 0, 1/0, -1/0
        f = Fraction(1,0)
        g = Fraction(1,0)
        self.assertTrue(f == g)

        f = Fraction(-1,0)
        g = Fraction(-1,0)
        self.assertTrue(f == g) 

        f = Fraction(0)
        g = Fraction(0)
        self.assertTrue(f == g)

        f = Fraction(2)
        g = Fraction(2)
        self.assertTrue(f == g)
