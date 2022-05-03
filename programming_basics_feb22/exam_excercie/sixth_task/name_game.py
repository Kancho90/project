max_points = 0
winner_name = ''

while True:
    name = input()
    current_points = 0
    if name == 'Stop':
        break

    for i in range(len(name)):
        number = int(input())
        if number == ord(name[i]):
            current_points += 10
        else:
            current_points += 2

    if current_points >= max_points:
        winner_name = name
        max_points = current_points



print(f'The winner is {winner_name} with {max_points} points!')