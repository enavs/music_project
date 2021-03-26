import datetime 

starter_date = datetime.datetime(1958, 8, 1)
# print(starter_date)

# end_date = starter_date+datetime.timedelta(days=1)
# print(end_date)

days = 365
years = 63
days_times_years = days*years
# print(days_times_years)

# for i in range(1, 36):
#     starter_date = starter_date + datetime.timedelta(days=1)
#     print(starter_date, starter_date.strftime("%u"), starter_date.strftime("%U"))


list_for_billboards = []
string_dates_for_billboards = []
for i in range(1, days_times_years):
    starter_date = starter_date + datetime.timedelta(days=1)
    day_of_week = starter_date.strftime("%u")
    if day_of_week == '7':
        list_for_billboards.append(starter_date)

        string_output = str(starter_date.year)+"-"+str("{:02d}".format(starter_date.month))+"-"+str("{:02d}".format(starter_date.day))
        string_dates_for_billboards.append(string_output)
    # print(string_output)
    # break

print(f"This is the min value: {min(list_for_billboards)} and this is the max value {max(list_for_billboards)}")
print()
print(list_for_billboards[0:2])
print(string_dates_for_billboards[0:20])
