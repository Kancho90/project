import sys

n = int(input())

max_number = -sys.maxsize
sum = 0

for i in range(n):
    current_number = int(input())
    sum += current_number

    if current_number > max_number:
        max_number = current_number


if max_number == sum - max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    diff = abs(sum - max_number * 2)
    print('No')
    print(f'Diff = {diff}')