def unpacking(filename):
    f=open(filename,'r')

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


def num_of_days_in_months(months_list):
    dict_of_days_in_months={}
    for month in months_list:
        if month not in dict_of_days_in_months.keys():
            dict_of_days_in_months[month] = 1
        else:
            dict_of_days_in_months[month] +=1
    return dict_of_days_in_months


def dict_of_dicts_month_number_weekday(months_list, days_num_list, weekdays_list):
    dict_of_days_in_months={}
    for month in months_list:
        if month not in dict_of_days_in_months.keys():
            dict_of_days_in_months[month] = {}
    for i in range(len(days_num_list)):
        dict_of_days_in_months[months_list[i]][days_num_list[i]] = weekdays_list[i]
    return dict_of_days_in_months

def dict_of_dicts_month_weekday_its_numbers(dictionar):
    new_dict ={}
    for month in dictionar.keys():
        new_dict[month] = {}
        for val in dictionar[month].values():
            new_dict[month][val] = [key for key in dictionar[month].keys() if dictionar[month][key]==val]
    return new_dict
