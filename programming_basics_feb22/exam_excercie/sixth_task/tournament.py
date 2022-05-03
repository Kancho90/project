days = int(input())
total_wins = 0
total_losses = 0
total_points = 0

for i in range(days):
    game = input()
    day_wins = 0
    day_loses = 0
    day_points = 0
    while game != 'Finish':
        result = input()
        if result == 'win':
            day_wins += 1
            day_points += 20
        elif result == 'lose':
            day_loses += 1

        game = input()
    if day_wins > day_loses:
        total_points += day_points * 1.1
        total_wins += 1
    else:
        total_points += day_points
        total_losses += 1
    day_points = 0
    day_loses = 0
    day_wins = 0
if total_wins > total_losses:
    print(f'You won the tournament! Total raised money: {total_points * 1.2:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_points:.2f}')


