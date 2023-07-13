import unittest
import main
from unittest.mock import patch, mock_open

class TestDictDates(unittest.TestCase):
    MONTHS = ['Jan','Jan','Feb','Feb','Apr']
    NUM_DAYS = ['1','2','6','7','29']
    WEEKDAYS = ['Sun','Mon','Mon','Tue','Sat']
    DICTIONAR_MONTHS_DAYS_WEEKDAYS = {'Jan':{'1':'Sun','2':'Mon'},'Feb':{'6':'Mon','7':'Tue'},'Apr':{'29':'Sat'}}

    def test_given_data_returns_three_lists_of_strings_in_correct_order(self):
        
        m=mock_open
        read_data = "Jan  1   Sun"
        with patch('__main__.open', mock_open(read_data=read_data)) as m:
            with open('test_dates.txt') as h:
                result = h.read()
        main.open_file_with_data = m

        
        result = main.unpack('test_dates.txt')
        expected = (['Jan'],['1'],['Sun'])
        self.assertEqual(expected,result)
    
    def test_given_months_return_dict(self):
        inp = self.MONTHS
        result = main.generate_dict_month_count_days(inp)
        self.assertIsInstance(result,dict)
    
    def test_given_months_return_dict_of_months_with_correct_number_of_days(self):
        inp = self.MONTHS
        result = main.generate_dict_month_count_days(inp)
        expected = {'Jan':2,'Feb':2,'Apr':1}
        self.assertDictEqual(result,expected)
    
    def test_given_months_num_of_days_and_weekdays_return_dict(self):
        inp1, inp2, inp3 = self.MONTHS,self.NUM_DAYS,self.WEEKDAYS
        result = main.generate_dict_of_dicts_month_number_weekday(inp1, inp2, inp3)
        self.assertIsInstance(result,dict)

    def test_given_months_num_of_days_and_weekdays_return_dict_of_dicts_with_correct_number_of_dicts(self):
        inp1, inp2, inp3 = self.MONTHS,self.NUM_DAYS,self.WEEKDAYS
        result = [val for val in main.generate_dict_of_dicts_month_number_weekday(inp1, inp2, inp3).values()]
        expected_len = 3
        self.assertEqual(len(result),expected_len)
        for element in result:
            self.assertIsInstance(element,dict)

    def test_given_months_num_of_days_and_weekdays_return_dict_of_dicts_with_correct_data(self):
        inp1, inp2, inp3 = self.MONTHS,self.NUM_DAYS,self.WEEKDAYS
        result = main.generate_dict_of_dicts_month_number_weekday(inp1, inp2, inp3)
        expected = self.DICTIONAR_MONTHS_DAYS_WEEKDAYS
        self.assertDictEqual(expected,result)
    

    def test_given_dictionary_of_dictionaries_retruns_dictionary(self):
        inp = self.DICTIONAR_MONTHS_DAYS_WEEKDAYS
        result = main.generate_dict_of_dicts_month_weekday_its_numbers(inp)
        self.assertIsInstance(result,dict)

    def test_given_dictionary_of_dictionaries_return_dict_of_dicts_with_correct_number_of_dicts(self):
        inp = self.DICTIONAR_MONTHS_DAYS_WEEKDAYS
        result = [val for val in main.generate_dict_of_dicts_month_weekday_its_numbers(inp).values()]
        expected_len = 3
        self.assertEqual(len(result),expected_len)
        for element in result:
            self.assertIsInstance(element,dict)

    def test_given_dictionary_of_dictionaries_return_dict_of_dicts_with_correct_data(self):
        inp = self.DICTIONAR_MONTHS_DAYS_WEEKDAYS
        result = main.generate_dict_of_dicts_month_weekday_its_numbers(inp)
        expected = {'Jan': {'Sun':['1'], 'Mon':['2']}, 'Feb':{'Mon':['6'],'Tue':['7']}, 'Apr': {'Sat':['29']}}
        self.assertDictEqual(expected,result)
