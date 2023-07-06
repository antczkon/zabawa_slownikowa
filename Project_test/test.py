import unittest
import main


class TestDictDates(unittest.TestCase):
    def test_given_data_returns_three_lists_of_strings_in_correct_order(self):
        result = main.unpacking('test_dates.txt')
        expected = (['Jan','Jan','Feb','Feb','Apr'],['1','2','6','7','29'],['Sun','Mon','Mon','Tue','Sat'])
        self.assertEqual(expected,result)
    
    def test_given_months_return_dict(self):
        inp = ['Jan','Jan','Feb','Feb','Apr']
        result = type(main.num_of_days_in_months(inp))
        dicto={}
        expected = type(dicto)
        self.assertEqual(expected,result)
    
    def test_given_months_return_dict_of_months_in_order(self):
        inp = ['Jan','Jan','Feb','Feb','Apr']
        result = list(main.num_of_days_in_months(inp).keys())
        expected = ['Jan','Feb','Apr']
        self.assertEqual(expected,result)

    def test_given_months_return_correct_num_of_days_in_each_month(self):
        inp = ['Jan','Jan','Feb','Feb','Apr']
        result = list(main.num_of_days_in_months(inp).values())
        expected = [2,2,1]
        self.assertEqual(expected,result)
    
    def test_given_months_num_of_days_and_weekdays_return_dict(self):
        inp1, inp2, inp3 = ['Jan','Jan','Feb','Feb','Apr'],['1','2','6','7','29'],['Sun','Mon','Mon','Tue','Sat']
        result = type(main.dict_of_dicts_month_number_weekday(inp1, inp2, inp3))
        dicto={}
        expected = type(dicto)
        self.assertEqual(expected,result)

    def test_given_months_num_of_days_and_weekdays_return_dict_of_dicts_with_correct_number_of_dicts(self):
        inp1, inp2, inp3 = ['Jan','Jan','Feb','Feb','Apr'],['1','2','6','7','29'],['Sun','Mon','Mon','Tue','Sat']
        result = [type(val) for val in main.dict_of_dicts_month_number_weekday(inp1, inp2, inp3).values()]
        dicto={}
        expected = [type(dicto), type(dicto), type(dicto)]
        self.assertEqual(expected,result)

    def test_given_months_num_of_days_and_weekdays_return_dict_of_dicts_with_correct_order_of_keys(self):
        inp1, inp2, inp3 = ['Jan','Jan','Feb','Feb','Apr'],['1','2','6','7','29'],['Sun','Mon','Mon','Tue','Sat']
        result = list(main.dict_of_dicts_month_number_weekday(inp1, inp2, inp3).keys())
        expected = expected = ['Jan','Feb','Apr']
        self.assertEqual(expected,result)
    
    def test_given_months_num_of_days_and_weekdays_return_dict_of_dicts_with_correct_order_of_keys_in_dicts(self):
        inp1, inp2, inp3 = ['Jan','Jan','Feb','Feb','Apr'],['1','2','6','7','29'],['Sun','Mon','Mon','Tue','Sat']
        dicts = list(main.dict_of_dicts_month_number_weekday(inp1,inp2,inp3).values())
        result = [[key for key in diction.keys()] for diction in dicts]      
        expected = [['1','2'],['6','7'],['29']]
        self.assertEqual(expected,result)
    
    def test_given_months_num_of_days_and_weekdays_return_dict_of_dicts_with_correct_order_of_values_in_dicts(self):
        inp1, inp2, inp3 = ['Jan','Jan','Feb','Feb','Apr'],['1','2','6','7','29'],['Sun','Mon','Mon','Tue','Sat']
        dicts = list(main.dict_of_dicts_month_number_weekday(inp1,inp2,inp3).values())
        result = [[val for val in diction.values()] for diction in dicts]      
        expected = [['Sun','Mon'],['Mon','Tue'],['Sat']]
        self.assertEqual(expected,result)

    def test_given_dictionary_of_dictionaries_retruns_dictionary(self):
        inp = {'Jan':{'1':'Sun','2':'Mon'},'Feb':{'6':'Mon','7':'Tue'},'Apr':{'29':'Sat'}}
        result = type(main.dict_of_dicts_month_weekday_its_numbers(inp))
        dicto={}
        expected = type(dicto)
        self.assertEqual(expected,result)

    def test_given_dictionary_of_dictionaries_return_dict_of_dicts_with_correct_number_of_dicts(self):
        inp = {'Jan':{'1':'Sun','2':'Mon'},'Feb':{'6':'Mon','7':'Tue'},'Apr':{'29':'Sat'}}
        result = [type(val) for val in main.dict_of_dicts_month_weekday_its_numbers(inp).values()]
        dicto={}
        expected = [type(dicto), type(dicto), type(dicto)]
        self.assertEqual(expected,result)

    def test_given_dictionary_of_dictionaries_return_dict_of_dicts_with_correct_order_of_keys(self):
        inp = {'Jan':{'1':'Sun','2':'Mon'},'Feb':{'6':'Mon','7':'Tue'},'Apr':{'29':'Sat'}}
        result = list(main.dict_of_dicts_month_weekday_its_numbers(inp).keys())
        expected = expected = ['Jan','Feb','Apr']
        self.assertEqual(expected,result)

    def test_given_dictionary_of_dictionaries_return_dict_of_dicts_with_correct_order_of_keys_in_dicts(self):
        inp = {'Jan':{'1':'Sun','2':'Mon'},'Feb':{'6':'Mon','7':'Tue'},'Apr':{'29':'Sat'}}
        dicts = list(main.dict_of_dicts_month_weekday_its_numbers(inp).values())
        result = [[key for key in diction.keys()] for diction in dicts]      
        expected = [['Sun','Mon'],['Mon','Tue'],['Sat']]
        self.assertEqual(expected,result)

    def test_given_dictionary_of_dictionaries_return_dict_of_dicts_with_correct_order_of_values_in_dicts(self):
        inp = {'Jan':{'1':'Sun','2':'Mon', '9':'Mon'},'Feb':{'6':'Mon','7':'Tue'},'Apr':{'29':'Sat'}}
        dicts = list(main.dict_of_dicts_month_weekday_its_numbers(inp).values())
        result = [list(diction.values()) for diction in dicts]      
        expected = [[['1'],['2','9']],[['6'],['7']],[['29']]]
        self.assertEqual(expected,result)