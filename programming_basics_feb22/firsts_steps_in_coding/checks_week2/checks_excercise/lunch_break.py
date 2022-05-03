import math

series_name = input()
episode_lenght = int(input())
break_lenght = int(input())

lunch_lenght = break_lenght / 8
relax_lenght = break_lenght / 4

time_left  = break_lenght - lunch_lenght - relax_lenght
enough_time = math.ceil(time_left - episode_lenght)
not_enought_time = math.ceil(episode_lenght - time_left)

if time_left >= episode_lenght:
    print(f'You have enough time to watch {series_name} and left with {enough_time} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need {not_enought_time} more minutes.")
