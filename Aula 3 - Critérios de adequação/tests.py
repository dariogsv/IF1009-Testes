import unittest
from area import circle_area, rectangle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        #Test area when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)

    def test_values(self):
        #Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)


    def test_type(self):
        #Make sure type errors are raised when necessary
        self.assertRaises(TypeError, circle_area, "-2")

class TestRectangleArea(unittest.TestCase):
    def test_area(self):
        #Test area when w>=0 and l>=0
        self.assertEqual(rectangle_area(2,3), 6)


if __name__ == '__main__':
    unittest.main()