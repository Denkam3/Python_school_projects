"""
This is for testing functions in physical_units_utils.py
"""

import unittest
from physical_units_utils import convert_speed, convert_temp

class TestPhysicalUnits (unittest.TestCase):
    def test_convert_speed(self):
        # test float, integer, lower/upper case for input
        self.assertAlmostEqual(convert_speed(2, "kph", "mph"), 1.242742384)
        self.assertAlmostEqual(convert_speed(5.4, "MPH", "kph"), 8.690436)
        self.assertEqual(convert_speed(100, "KPH", "kph"), 100)

    def test_speed_error(self):
        # test value error
        with self.assertRaises(ValueError):
            convert_speed("one","kph", "mph")
        with self.assertRaises(ValueError):
            convert_speed(100, "kp/h", "miles")


    def test_convert_temp(self):
        # test float, integer, lower/upper case for input
        self.assertAlmostEqual(convert_temp(5, "°C", "K"), 278.15)
        self.assertAlmostEqual(convert_temp(293.55, "k", "°C"), 20.4)
        self.assertAlmostEqual(convert_temp(100, "°c", "K"), 373.15)

    def test_temp_error(self):
        # test value error
        with self.assertRaises(ValueError):
            convert_temp("room_temp", "°C", "K")
        with self.assertRaises(ValueError):
            convert_temp(20, "degrees", "Kelvin")

if __name__ == "__main__":
    unittest.main()
