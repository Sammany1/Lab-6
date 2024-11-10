import unittest
from calculator import Calc

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = Calc.add(3, 7)
        self.assertEqual(result, 10)
        
        result = Calc.add(-1, 1)
        self.assertEqual(result, 0)
        
        result = Calc.add(-1, -1)
        self.assertEqual(result, -2)
