#https://github.com/macy-tam/lab10-MT-NB.git
#Partner 1: Macy Tam
#Partner 2: Nicholas Batchelor
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5, 5), 10)
        self.assertEqual(add(4, 8), 12)
        self.assertEqual(add(13, 25), 38)
    #     fill in code

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(23, 5), 18)
        self.assertEqual(subtract(12, 7), 5)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
    #     fill in code
        self.assertEqual(mul(1,5), 5)
        self.assertEqual(mul(-2,-7), 14)
        self.assertEqual(mul(12,-10), -120)

    def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################
        self.assertEqual(div(2,6), 3)
        self.assertEqual(div(12,-60),-5 )
        self.assertEqual(div(-10,-30), 3)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 2)
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 4), 2)
        self.assertAlmostEqual(logarithm(3, 3), 1)
        self.assertAlmostEqual(logarithm(2, 8), 3)
    #     fill in code

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-1, 5)
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
        with self.assertRaises(ValueError):
            logarithm(0,78)

    def test_hypotenuse(self): # 3 assertions
    #     fill in code
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(5,12), 13)
        self.assertEqual(hypotenuse(6,8), 10)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################
        with self.assertRaises(ValueError):
            square_root(-99)
        self.assertEqual(square_root(64), 8)
        self.assertEqual(square_root(9), 3)

# Do not touch this
if __name__ == "__main__":
    unittest.main()