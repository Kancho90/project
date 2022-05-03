name = input()
games = int(input())

w = 0
l = 0
d = 0

for i in range(games):
    result = input()
    if result == 'W':
        w += 1
    elif result == 'L':
        l += 1
    elif result == 'D':
        d += 1

total = 3 * w + d
if games == 0:
    print(f"{name} hasn't played any games during this season.")
else:
    print(f'{name} has won {total} points during this season.')
    print('Total stats:')
    print(f'## W: {w}')
    print(f'## D: {d}')
    print(f'## L: {l}')
    print(f'Win rate: {w / games * 100:.2f}%')