import calendar
import datetime

# c = calendar.Calendar(0)
# print(c.monthdayscalendar(2020, 1))
#
# c = calendar.TextCalendar(firstweekday=0)
# print(c.formatyear(2020))

# today = datetime.datetime.today()
# print(today.year)
# print(today.month)
# print(today.day)


# date = calendar.monthrange(today.year, today.month)
# print(type(date))
# print('date:', date)

# date1 = c.monthdayscalendar(today.year, today.month)
# date1 = c.itermonthdates(today.year, today.month)
# print(date1)


def date_by_adding_business_days(from_date, add_days):
    while add_days > 0:
        from_date += datetime.timedelta(days=1)
        # print(from_date)
        weekday = from_date.weekday()
        if weekday >= 5:
            continue
        add_days -= 1

    print(from_date.strftime('%d.%m.%Y'))
    return from_date.strftime('%d.%m.%Y')

if __name__ == '__main__':
    from_date = datetime.datetime.today()
    add_days = 10

    date_by_adding_business_days(from_date, add_days)