import math

tournaments = int(input())
starting_points = int(input())
wins = 0
points = 0

for i in range(tournaments):
    result = input()
    if result == 'W':
        points +=2000
        wins += 1
    elif result == 'F':
        points += 1200
    else:
        points += 720

print(f'Final points: {points + starting_points}')
print(f'Average points: {math.floor(points / tournaments)}')
print(f'{wins / tournaments * 100:.2f}%')