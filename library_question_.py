ex_day=int(input("enter a day"))
re_day=int(input("enter a day"))
ex_month=int(input("enter a month"))
re_month=int(input("enter a month"))
ex_year=int(input("enter a year"))
re_year=int(input("enter a year"))
if re_day<=ex_day or re_month<=ex_month or re_year<=ex_year:
    print(0)
if re_day>ex_day :
    print(15*(re_day-ex_day))
if re_month>ex_month:
    print(500*(re_month-ex_month))
if re_year>ex_year:
    print(1000*(re_year-ex_year))
else:
    print("nothing")