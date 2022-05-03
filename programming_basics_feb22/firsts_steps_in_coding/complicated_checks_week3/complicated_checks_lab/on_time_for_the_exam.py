exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

total_exam = exam_hour * 60 + exam_minutes
total_arrival = arrival_minute + arrival_hour *  60
time_left = abs(total_arrival - total_exam)

if total_arrival > total_exam:
    print('Late')
    if time_left < 60:
        print(f'{time_left} minutes after the start')
    elif time_left == 60:
        print(f'1:00 hours after the start')
    else:
        print(f'{time_left // 60}:{time_left % 60:02d} hours after the start')
elif total_arrival == total_exam  or time_left <= 30:
    print('On time')
    print(f'{time_left} minutes before the start')
else:
    print('Early')
    if time_left < 60:
        print(f'{time_left} minutes before the start')
    elif time_left == 60:
        print(f'1:00 hours  before the start')
    else:
        print(f'{time_left // 60}:{time_left % 60:02d} hours before the start')