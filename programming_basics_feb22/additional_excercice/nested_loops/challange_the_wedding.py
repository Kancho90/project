man = int(input())
women = int(input())
tables = int(input())

tables_taken = 0

for m in range(1, man + 1):
    for w in range(1, women + 1):
        print(f'({m} <-> {w})', end= ' ')
        tables_taken += 1
        if tables == tables_taken:
            break
    if tables == tables_taken:
        break
