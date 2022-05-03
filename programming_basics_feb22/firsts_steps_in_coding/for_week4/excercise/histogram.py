n = int(input())
upto200 = 0
upto399 = 0
upto599 = 0
upto799 = 0
above799 = 0

for i in range(n):
    number = int(input())

    if number < 200:
        upto200 += 1
    elif 200 <= number < 400:
        upto399 += 1
    elif 400 <= number < 600:
        upto599 += 1
    elif 600 <= number < 800:
        upto799 += 1
    else:
        above799 += 1

print(f'{upto200 / n * 100:.2f}%')
print(f'{upto399 / n * 100:.2f}%')
print(f'{upto599 / n * 100:.2f}%')
print(f'{upto799 / n * 100:.2f}%')
print(f'{above799 / n * 100:.2f}%')


