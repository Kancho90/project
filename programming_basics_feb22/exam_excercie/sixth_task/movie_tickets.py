a1 = int(input())
a2 = int(input())
n = int(input())

for i in range (a1, a2):
    if i % 2 != 0:
        symbol1 = chr(i)
        for s2 in range(1, n):
            r3 = n / 2
            for s3 in range (1, int(r3)):
                symbol4 = ord(symbol1)
                if (s2 + s3 + symbol4) % 2 != 0:
                    print(f'{symbol1}-{s2}{s3}{symbol4}')


