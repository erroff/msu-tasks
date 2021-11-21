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
        p = [1, 6, 0, 5, 6, 9]
        self.assertEqual(find(p, 16), -1)

    def test_multiple_values(self):
        p = [1, 6, 0, 5, 6, 9]
        self.assertEqual(find(p, 6), 1)


class MinTest(unittest.TestCase):

    def test_positive_value(self):
        p = [1, 2, 3, 4, 5]
        self.assertEqual(my_min(p), 1)

    def test_negative_value(self):
        p = [-1, -2, -3, -4, -5]
        self.assertEqual(my_min(p), -5)


class MaxTest(unittest.TestCase):

    def test_positive_value(self):
        p = [1, 2, 3, 4, 5]
        self.assertEqual(my_max(p), 5)

    def test_negative_value(self):
        p = [-1, -2, -3, -4, -5]
        self.assertEqual(my_max(p), -1)


class SumTest(unittest.TestCase):
    def test_positive_value(self):
        p = [1, 2, 3, 4, 5]
        self.assertEqual(my_sum(p), 15)

    def test_negative_value(self):
        p = [-1, -2, -3, -4, -5]
        self.assertEqual(my_sum(p), -15)

    def test_zero_value(self):
        p = [0]
        self.assertEqual(my_sum(p), 0)


class RevertTest(unittest.TestCase):

    def test_case1(self):
        p = [1, 2, 3, 4, 5]
        self.assertEqual(revert(p), [5, 4, 3, 2, 1])

    def test_case2(self):
        p = [0, 0, 1, 1, 2, 2]
        self.assertEqual(revert(p), [2, 2, 1, 1, 0, 0])

    def test_case3(self):
        p = [0]
        self.assertEqual(revert(p), [0])


class UniqueTest(unittest.TestCase):
    def test_case1(self):
        p = [0, 0, 1, 1, 2, 2]
        self.assertEqual(unique(p), [0, 1, 2])

    def test_case2(self):
        p = [0, 1, 2, 0, 1, 2]
        self.assertEqual(unique(p), [0, 1, 2])

    def test_case3(self):
        p = [0, 1, 2]
        self.assertEqual(unique(p), [0, 1, 2])


class CapitalizeTest(unittest.TestCase):

    def test_case1(self):
        s = 'ex@mplE StrI#g'
        self.assertEqual(capitalize(s), 'Ex@mple stri#g')

    def test_case2(self):
        s = 'EXAMPLE STRING'
        self.assertEqual(capitalize(s), 'Example string')

    def test_case3(self):
        s = ''
        self.assertEqual(capitalize(s), '')


class LowerTest(unittest.TestCase):
    def test_case1(self):
        s = 'ex@mplE StrI#g'
        self.assertEqual(lower(s), 'ex@mple stri#g')

    def test_case2(self):
        s = 'EXAMPLE STRING'
        self.assertEqual(lower(s), 'example string')

    def test_case3(self):
        s = ''
        self.assertEqual(lower(s), '')


class UpperTest(unittest.TestCase):
    def test_case1(self):
        s = 'ex@mplE StrI#g'
        self.assertEqual(upper(s), 'EX@MPLE STRI#G')

    def test_case2(self):
        s = 'example string'
        self.assertEqual(upper(s), 'EXAMPLE STRING')

    def test_case3(self):
        s = ''
        self.assertEqual(upper(s), '')


class ReplaceTest(unittest.TestCase):

    def test_replace_symbol(self):
        s = 'ex@mplE StrI#g'
        self.assertEqual(replace(s, '#', 'n'), 'ex@mplE StrIng')

    def test_replace_word(self):
        s = 'example string'
        self.assertEqual(replace(s, 'string', 'STRING'), 'example STRING')

    def test_replace_nothing(self):
        s = 'hello world'
        self.assertEqual(replace(s, '', ''), 'hello world')


class SwapcaseTest(unittest.TestCase):

    def test_case1(self):
        s = 'ex@mplE StrI#g'
        self.assertEqual(swapcase(s), 'EX@MPLe sTRi#G')

    def test_case2(self):
        s = 'example string'
        self.assertEqual(swapcase(s), 'EXAMPLE STRING')

    def test_case3(self):
        s = ''
        self.assertEqual(swapcase(s), '')


class SplitTest(unittest.TestCase):

    def test_case1(self):
        s = 'ex@mplE StrI#g'
        self.assertEqual(my_split(s, ' '), ['ex@mplE', 'StrI#g'])

    def test_case2(self):
        s = 'example_string'
        self.assertEqual(my_split(s, '_'), ['example', 'string'])

    def test_case3(self):
        s = ''
        self.assertEqual(my_split(s, '_'), [''])


if __name__ == '__main__':
    unittest.main(verbosity=0)
