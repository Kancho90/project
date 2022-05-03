floors = int(input())
spaces = int(input())

for i in range(floors, 0, -1):
    app = 0
    office = 0
    large = 0
    if i == floors:
        for y in range(0, spaces):
            print(f'L{i}{large}', end = " ")
            large += 1
    elif i % 2 != 0:
        for y in range(0, spaces):
            print(f'A{i}{app}', end = " ")
            app += 1
    else:
        for y in range(0, spaces):
            print(f'O{i}{office}',end = " ")
            office += 1
    print()
