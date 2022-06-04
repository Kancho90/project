number = int(input())

n = str(number)
m = sorted(n, reverse=True)
for test, digit in enumerate(m):
    print(digit,end='')
