n1 = input()
n2 = input()

for i in range(int(n1[0]), int(n2[0]) + 1):
    for i2 in range(int(n1[1]), int(n2[1]) + 1):
        for i3 in range(int(n1[2]), int(n2[2]) + 1):
            for i4 in range(int(n1[3]), int(n2[3]) + 1):
                if i % 2 != 0 and i2 % 2 != 0 and i3 % 2 != 0 and i4 % 2 != 0:
                    print(f'{i}{i2}{i3}{i4}', end= " ")
