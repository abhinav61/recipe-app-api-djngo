from django.test import TestCase
from app.calc import cal, sub


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(cal(3, 8), 11)

    def test_subtract_numbers(self):
        """Test whether the two numbers are subtracted and returned"""
        self.assertEqual(sub(2, 3), 1)
