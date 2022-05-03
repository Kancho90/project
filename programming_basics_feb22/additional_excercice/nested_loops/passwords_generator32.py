n = int(input())
l = int(input())

letter = ord('a')
letter2 = letter + l

for i1 in range(1, n + 1):
    for i2 in range(1, n + 1):
        for i3 in range(letter, letter2):
            for i4 in range(letter, letter2):
                for i5 in range(1,n + 1):
                    if i5 > i1 and i5 > i2:
                        a1 = chr(i3)
                        a2 = chr(i4)
                        print(f'{i1}{i2}{a1}{a2}{i5}', end=' ')