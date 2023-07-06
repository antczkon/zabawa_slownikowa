def unpack_dates(filename):
    f = open(filename, 'r')

    months=[]
    num_days = []
    weekdays =[]

    for row in f:
        temp = row.split()
        month, num_day, weekday = temp[0], temp[1], temp[2]
        months.append(month)
        num_days.append(num_day)
        weekdays.append(weekday)
    return months, num_days, weekdays

def num_of_days_task(months):
    months_with_numbers = {}
    for i in range (len(months)):
        months_with_numbers[months[i]] = months.count(months[i])
    return months_with_numbers

def dict_month_num_weekday_task(months, num_days, weekdays):
    dict = {}
    for i in months:
        dict[i]={}

    for i in range(len(num_days)):
        dict[months[i]][num_days[i]]=weekdays[i]

    return dict

def dict_month_weekday_nums_task(dict):
    new_dict = {}
    for month in dict.keys():
        new_dict[month] = {}
        for weekday in dict[month].values():
            new_dict[month][weekday] = [num_day for num_day in dict[month].keys() if dict[month][num_day]==weekday]
    return new_dict

months, num_days, weekdays = unpack_dates('dates.txt')
old=dict_month_num_weekday_task(months, num_days, weekdays)
new=dict_month_weekday_nums_task(old)
print(new['May'])