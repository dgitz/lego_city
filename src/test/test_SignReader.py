import unittest

import sys
 
# setting path
sys.path.append('../')
 
# importing
from SignReader import SignReader,Sign

class TestSignReader(unittest.TestCase):
    def test_no_sign(self):
        reader = SignReader()
        actual = reader.read_sign(0)
        expected = Sign.NONE
        self.assertEqual(actual, expected)