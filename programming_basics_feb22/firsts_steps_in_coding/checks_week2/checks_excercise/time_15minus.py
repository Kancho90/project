hours = int(input())
minutes = int(input())

minutes_added = minutes + 15
if minutes_added >= 60:
    hours_result = hours + 1
    minutes_result = minutes_added - 60
elif minutes_added < 60:
    hours_result = hours
    minutes_result = minutes_added

if hours_result == 24:
    hours_result = hours_result - 24
else:
    hours_result = hours_result



if minutes_result < 10:
    print(f'{hours_result}:0{minutes_result}')
elif minutes_result >= 10:
    print(f'{hours_result}:{minutes_result}')
