# #exercise day 10 -1
#
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(year, month):
#
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     months = len(month_days)
#     month_listed = month - 1
#
#     # if is_leap(year) == True:
#     #     if month_listed != 1:
#     #         return month_days[month_listed]
#     #     else:
#     #         return month_days[month_listed] + 1
#     # else:
#     #     return month_days[month_listed]
#     if is_leap(year) == True and month == 02:
#         return 29
#     return month_days[month - 1]
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

##########################################################################################################

