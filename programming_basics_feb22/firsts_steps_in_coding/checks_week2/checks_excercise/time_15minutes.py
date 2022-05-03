hours = int(input())
minutes = int(input())

total_minutes = hours * 60 + minutes
total_minutes += 15

hours_result = total_minutes // 60
minutes_result = total_minutes % 60

if hours_result > 23:
    hours_result -= 24
    print(f'{hours_result}:{minutes_result:02d}')
else:
    print(f'{hours_result}:{minutes_result:02d}')