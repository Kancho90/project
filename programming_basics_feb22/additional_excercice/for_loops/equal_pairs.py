import sys

n = int(input())
sum1 = 0
sum2 = 0

for num in range(n):
    if num % 2 == 0:
        num1 = int(input())
        num2 = int(input())
        sum1 = num1 + num2
    else:
        num3 = int(input())
        num4 = int(input())
        sum2 = num3 + num4

if n == 1:
    sum2 = sum1

if sum1 == sum2:
    print(f'Yes, value={sum1}')
else:
    print(f'No, maxdiff={abs(sum2-sum1)}')
