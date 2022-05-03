n = int(input())

red_balls = 0
orange_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_color = 0
total_points = 0
black = 0

for i in range(n):
    color = input()

    if color == 'red':
        red_balls += 1
        total_points += 5
    elif color == 'orange':
        orange_balls += 1
        total_points += 10
    elif color == 'yellow':
        yellow_balls += 1
        total_points += 15
    elif color == 'white':
        white_balls += 1
        total_points += 20
    elif color == 'black':
        total_points /= 2
        black += 1
    else:
        other_color += 1
print(f'Total points: {int(total_points)}')
print(f'Red balls: {red_balls}')
print(f'Orange balls: {orange_balls}')
print(f'Yellow balls: {yellow_balls}')
print(f'White balls: {white_balls}')
print(f'Other colors picked: {other_color}')
print(f'Divides from black balls: {black}')