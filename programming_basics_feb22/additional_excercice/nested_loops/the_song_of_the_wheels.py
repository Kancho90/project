m = int(input())
count = 0
password = ''
passfound = False

for i1 in range(1,10):
    for i2 in range(1,10):
        if i1 < i2:
            for i3 in range(1,10):
                for i4 in range(1,10):
                    if i3 > i4 and (i1 * i2) + (i3*i4) == m:
                        count += 1
                        print(f'{i1}{i2}{i3}{i4}', end= ' ')
                        if count == 4:
                            passfound = True
                            password = str(i1) + str(i2) + str(i3) + str(i4)

if passfound:
    print()
    print(f'Password: {password}')
else:
    print()
    print('No!')