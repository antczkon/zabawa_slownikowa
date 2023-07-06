filename = 'dates.txt'
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

months_with_numbers = {}
for i in range (len(months)):
    months_with_numbers[months[i]] = months.count(months[i])
print(months_with_numbers)

dict = {}
for i in months:
    dict[i]={}

for i in range(len(num_days)):
    dict[months[i]][num_days[i]]=weekdays[i]
print(dict['May'])

new_dict = {}
for month in dict.keys():
    new_dict[month] = {}
    for weekday in dict[month].values():
       new_dict[month][weekday] = [num_day for num_day in dict[month].keys() if dict[month][num_day]==weekday]
print(new_dict['May'])
