time = int(input())
scenes = int(input())
lenght = int(input())

preparation_time = time * 0.15
total_time = preparation_time + scenes * lenght

if time >= total_time:
    time_left = time - total_time
    print(f'You managed to finish the movie on time! You have {round(time_left)} minutes left!')
else:
    time_needed = total_time - time
    print(f'Time is up! To complete the movie you need {round(time_needed)} minutes.')