time = int(input())
day = input()

# if day == "Sunday":
#     print('closed')
# elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
#     if 10 <= time <= 18:
#         print("open")
#     else:
#         print('closed')

working_days = ['Monday', 'Tueday', 'Wedensday', 'Thursday', 'Friday', 'Saturday']
if day in working_days and 10 <= time <=18:
    print('open')
else:
    print('closed')
