n1 = int(input())
n2 = int(input())

for i1 in range(n1, n2 + 1):
    for i2 in range(n1, n2 + 1):
        for i3 in range(n1, n2 + 1):
            if (i2 + i3) % 2 == 0:
                for i4 in range(n1, n2 + 1):
                    if i1 > i4:
                        if i1 % 2 == 0 and i4 % 2 != 0:
                            print(f'{i1}{i2}{i3}{i4}', end=" ")
                        elif i1 % 2 != 0 and i4 % 2 == 0:
                            print(f'{i1}{i2}{i3}{i4}', end=" ")