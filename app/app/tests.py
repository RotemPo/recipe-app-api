"""
Sample test
"""

from django.test import SimpleTestCase  # type: ignore
from app import calc


class CalcTest(SimpleTestCase):
    # tests class
    def test_add(self):
        res = calc.add(4, 7)
        self.assertEqual(res, 11)

    def test_sub(self):
        res = calc.sub(11, 4)
        self.assertEqual(res, 7)
