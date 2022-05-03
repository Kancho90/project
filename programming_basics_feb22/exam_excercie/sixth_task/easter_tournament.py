kozunaci = int(input())
winner = ''
winner_points = 0
for i in range(kozunaci):
    name = input()
    current_points = 0
    while True:
        points = input()
        if points == 'Stop':
            print(f'{name} has {current_points} points.')
            if current_points > winner_points:
                winner = name
                winner_points = current_points
                print(f'{name} is the new number 1!')
            break
        current_points += int(points)

print(f'{winner} won competition with {winner_points} points!')