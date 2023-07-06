def unpacking(filename):
    f=open(filename,'r')

    months=[]
    days_num=[]
    weekday_names=[]

    for row in f:
        month,day_num,weekday_name=row[0], row[1], row[2]
        months.append(month)
        days_num.append(day_num)
        weekday_names.append(weekday_name)
    return 'a'