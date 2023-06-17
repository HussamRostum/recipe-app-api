"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(10, 6)

        self.assertEqual(res, 16)

    def test_sub_numbers(self):
        """Test adding numbers together."""
        res = calc.sub(10, 15)
        self.assertEqual(res, 5)
        