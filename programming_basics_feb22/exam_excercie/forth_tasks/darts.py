name = input()

success = 0
failure = 0
remaining_points = 301

while True:
    sector = input()
    if sector == 'Retire':
        break
    points = int(input())
    if sector == 'Single':
        points = points
    elif sector == 'Double':
        points *= 2
    else:
        points *= 3

    if remaining_points - points > 0:
        success += 1
        remaining_points -= points
    elif remaining_points - points == 0:
        success += 1
        remaining_points = 0
        break
    else:
        failure += 1

if remaining_points > 0:
    print(f'{name} retired after {failure} unsuccessful shots.')
else:
    print(f'{name} won the leg with {success} shots.')