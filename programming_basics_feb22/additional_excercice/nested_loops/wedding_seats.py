last_sector = input()
rows = int(input())
seats = int(input())

total_seats = 0


for s in range(ord('A'), ord(last_sector) + 1):
    for r in range(1, rows + 1):
        lastletter = ord('a')
        if r % 2 == 0:
            for s1 in range(1, seats + 3):
                print(f'{chr(s)}{r}{chr(lastletter)}')
                lastletter += 1
                total_seats += 1
        else:
            for s1 in range(1, seats + 1):
                print(f'{chr(s)}{r}{chr(lastletter)}')
                lastletter += 1
                total_seats += 1
    rows += 1

print(total_seats)