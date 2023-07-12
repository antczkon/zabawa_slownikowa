import collections

def open_file_with_data(filename):
    f=open(filename,'r')
    return f

def unpack(filename):

    f = open_file_with_data(filename)

    months=[]
    days_num=[]
    weekday_names=[]

    for row in f:
        row = row.split()
        month,day_num,weekday_name=row[0], row[1], row[2]
        months.append(month)
        days_num.append(day_num)
        weekday_names.append(weekday_name)
    return months, days_num, weekday_names


def generate_dict_month_count_days(months_list):

    dict_of_days_in_months=collections.defaultdict(int)
    for month in months_list:
        dict_of_days_in_months[month] += 1
    return dict_of_days_in_months


def generate_dict_of_dicts_month_number_weekday(months_list, days_num_list, weekdays_list):

    dict_of_days_in_months=collections.defaultdict(int)
    for month in months_list:
        dict_of_days_in_months[month] = collections.defaultdict(int)
    
    elements = zip(months_list,days_num_list,weekdays_list)
    
    for element in elements:
        dict_of_days_in_months[element[0]][element[1]] = element[2]
    return dict_of_days_in_months

def generate_dict_of_dicts_month_weekday_its_numbers(dictionar):
    
    new_dict =collections.defaultdict(int)
    for month in dictionar.keys():
        new_dict[month] = collections.defaultdict(int)
        for val in dictionar[month].values():
            new_dict[month][val] = [key for key in dictionar[month].keys() if dictionar[month][key]==val]
    return new_dict
