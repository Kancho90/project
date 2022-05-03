tournament = input()
wins = 0
losses = 0

while tournament != 'End of tournaments':
    n = int(input())
    for i in range(1, n + 1):
        desi = int(input())
        team2 = int(input())
        diff = abs(desi - team2)
        if desi > team2:
            wins += 1
            print(f'Game {i} of tournament {tournament}: win with {diff} points.')
        else:
            losses += 1
            print(f'Game {i} of tournament {tournament}: lost with {diff} points.')

    tournament = input()

total = wins + losses
print(f'{wins / total * 100:.2f}% matches win')
print(f'{losses / total * 100:.2f}% matches lost')