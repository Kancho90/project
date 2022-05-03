import sys

n = int(input())

oddsum = 0
oddmin = sys.maxsize
oddmax = -sys.maxsize
evensum = 0
evenmin = sys.maxsize
evenmax = -sys.maxsize

for i in range(1, n+1):
    number = float(input())
    if i % 2 != 0:
        oddsum += number
        if number < oddmin:
            oddmin = number
        if number > oddmax:
            oddmax = number
    else:
        evensum += number
        if number < evenmin:
            evenmin = number
        if number > evenmax:
            evenmax = number

if n == 0:
    print(f'OddSum={oddsum:.2f},')
    print(f'OddMin=No,')
    print(f'OddMax=No,')
    print(f'EvenSum={evensum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
elif n == 1:
    print(f'OddSum={oddsum:.2f},')
    print(f'OddMin={oddmin:.2f},')
    print(f'OddMax={oddmax:.2f},')
    print(f'EvenSum={evensum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
else:
    print(f'OddSum={oddsum:.2f},')
    print(f'OddMin={oddmin:.2f},')
    print(f'OddMax={oddmax:.2f},')
    print(f'EvenSum={evensum:.2f},')
    print(f'EvenMin={evenmin:.2f},')
    print(f'EvenMax={evenmax:.2f}')
