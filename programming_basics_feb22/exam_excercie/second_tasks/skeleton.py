minutes = int(input())
seconds = int(input())
lenght = float(input())
seconds_per100 = int(input())

total_control_time = minutes * 60 + seconds
time_penalty = lenght / 120  * 2.5
total_time = lenght / 100  * seconds_per100 - time_penalty

if total_time <= total_control_time:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {total_time:.3f}.')
else:
    seconds_slower = total_time - total_control_time
    print(f'No, Marin failed! He was {seconds_slower:.3f} second slower.')