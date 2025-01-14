import unittest
from health_utils import calculate_bmi, calculate_bmr
from app import app
import json

class TestHealthCalculator(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
        with self.assertRaises(ValueError):
            calculate_bmi(0, 70)
    
    def test_calculate_bmr(self):
        self.assertAlmostEqual(
            calculate_bmr(175, 70, 30, 'male'),  # Inputs: height, weight, age, gender
            1695.67,  # Correct expected BMR value
            places=2  # Allowing comparison with 2 decimal places
        )
        self.assertAlmostEqual(
            calculate_bmr(165, 55, 25, 'female'),
            1359.10,
            places=2
        )

if __name__ == '__main__':
    unittest.main()
