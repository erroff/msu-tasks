import unittest
import sys
import os
if os.path.join(sys.path[0], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0], '..'))
from simple.main import *
__unittest = True


class SortTest(unittest.TestCase):

    def test_positive(self):
        p = [6, 4, 3, 1, 8]
        self.assertEqual(sort(p), sorted(p))

    def test_with_negative(self):
        p = [6, 4, 3, 1, -1, -6, 8]
        self.assertEqual(sort(p), sorted(p))

    def test_with_zeros(self):
        p = [0, 5, 0, 4, -8]
        self.assertEqual(sort(p), sorted(p))


class FindTest(unittest.TestCase):

    def test_present_in_list(self):
        p = [1, 6, 0, 5, 'none', []]
        self.assertEqual(find(p, []), p.index([]))

    def test_value_not_in_list(self):
        p = [1, 6, 0, 5, 'none', []]
        self.assertEqual(find(p, 16), -1)


if __name__ == '__main__':
    unittest.main(verbosity=0)
