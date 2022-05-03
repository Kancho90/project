n = int(input())

for i1 in range(1, 10):
    for i2 in range(1,10):
        if n % (i1 + i2) == 0:
            for i3 in range(1, 10):
                for i4 in range(1, 10):
                    if (i1 + i2) == (i3 + i4):
                        print(f'{i1}{i2}{i3}{i4}', end= ' ')