from django.shortcuts import render





# import datetime
# import calendar
# dt = datetime
# c = calendar
#
#
# first_date = dt.date(2022, 4, 22)
# last_date = dt.date(2022, 6, 12)
#
#
# def last_of_the_month(x_date):
#     return c.monthrange(x_date.year, x_date.month)[1]
#
#
# def days_of_holiday(begin, end):
#     if begin.month == end.month:
#         days = (end.day - begin.day) + 1
#     elif (begin.month + 1) == end.month:
#         first_month_days = (last_of_the_month(begin) - begin.day) + 1
#         second_month_days = end.day
#         days = first_month_days + second_month_days
#     elif (begin.month + 2) == end.month:
#         first_month_days = (last_of_the_month(begin) - begin.day) + 1
#         second_month_days = c.monthrange(begin.year, begin.month + 1)[1]
#         third_month_days = end.day
#         days = first_month_days + second_month_days + third_month_days
#     return days
#
#
# print(days_of_holiday(first_date, last_date))