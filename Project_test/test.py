import unittest
import main


class TestDictDates(unittest.TestCase):
    def test_given_data_returns_three_lists_of_strings_in_correct_order(self):
        result = main.unpacking('test_dates.txt')
        expected = (['Jan','Jan','Feb','Feb','Apr'],['1','2','6','7','29'],['Sun','Mon','Mon','Tue','Sat'])
        self.assertEqual(expected,result)