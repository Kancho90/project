import math

name = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
runtime = float (input())

runtime_with_commercials = runtime * 1.2
extra_minutes = number_of_seasons * 10
total_episodes = runtime_with_commercials * number_of_episodes * number_of_seasons
total = total_episodes + extra_minutes
total_answer = math.floor(total)

print(f'Total time needed to watch the {name} series is {total_answer} minutes.')