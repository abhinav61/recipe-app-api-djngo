from django.test import TestCase
from app.calc import cal

class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(cal(3,8),11)