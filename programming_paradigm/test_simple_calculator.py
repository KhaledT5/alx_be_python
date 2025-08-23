import unittest 
from simple_calculator.py import SimpleCalculator

class TestSimpleCalculator(unittest, TestCase):
    def setUp(self):
        """Set up a fresh calculator before each test."""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2,3), 5)
        self.assertEqual(self.calc.add(-1,1), 0)
        self.assertEqual(self.calc.add(0,0), 0)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(6,5), 1)
        self.assertEqual(self.calc.subtract(5,6), -1)
        self.assertEqual(self.calc.subtract(0,2), -2)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,1), 2)
        self.assertEqual(self.calc.multiply(-1,1), -1)
        self.assertEqual(self.calc.multiply(0,1), 0)
        
    def test_division(self):
        self.assertEqual(self.calc.divide(4,2), 2)
        self.assertAlmostEqual(self.calc.divide(5, 2), 3.5)
        self.assertIsNone(self.calc.divide(9,0))        
if __name__ == "__main__":
    unittest.main()