import unittest
from main import calculate_average

#tests
class AverageNumbersTestCase(unittest.TestCase):
    def test_average_normal_list(self):
            self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)

    def test_average_single_number(self):
            self.assertEqual(calculate_average([10]), 10)

    def test_average_empty_list(self):
            self.assertIsNone(calculate_average([]))

    def test_average_with_floats(self):
            self.assertEqual(calculate_average([1.5, 2.5, 3.5]), 2)

    def test_average_with_negatives(self):
            self.assertEqual(calculate_average([-1, -2, -3]), -2)

    def test_average_rounding_up(self):
            self.assertEqual(calculate_average([1, 2]), 2)

    def test_average_rounding_down(self):
            self.assertEqual(calculate_average([1, 1, 2]), 1)