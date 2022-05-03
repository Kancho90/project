games = int(input())

hs = 0
ow = 0
fn = 0
others = 0

for i in range(games):
    name = input()
    if name == 'Hearthstone':
        hs += 1
    elif name == 'Fornite':
        fn += 1
    elif name == 'Overwatch':
        ow += 1
    else:
        others += 1

print(f'Hearthstone - {hs / games * 100:.2f}%')
print(f'Fornite - {fn / games * 100:.2f}%')
print(f'Overwatch - {ow / games * 100:.2f}%')
print(f'Others - {others / games * 100:.2f}%')