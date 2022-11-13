"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """test calc"""

    def test_add_nubers(self):
        """test add numbers"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """ test subtract"""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
