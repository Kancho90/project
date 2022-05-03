import math

time_first = int(input())
time_second = int(input())
time_third = int(input())
total_time = time_first + time_second + time_third

total_minutes = total_time // 60
total_seconds = total_time % 60
minutes = math.floor(total_minutes)

if total_seconds < 10:
    print(f'{minutes}:0{total_seconds}')
else:
    print (f'{minutes}:{total_seconds}')