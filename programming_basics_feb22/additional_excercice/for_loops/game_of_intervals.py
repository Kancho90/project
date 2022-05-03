rounds = int(input())

total = 0
range9 = 0
range19 = 0
range29 = 0
range39 = 0
range50 = 0
invalid = 0

for i in range (rounds):
    result = int(input())
    if result < 0 or result > 50:
        total = total / 2
        invalid += 1
    elif 0 <= result < 10:
        total += 0.2 * result
        range9 += 1
    elif 9 < result < 20:
        total += 0.3 * result
        range19 += 1
    elif 19 < result < 30:
        total += 0.4 * result
        range29 += 1
    elif 29 < result < 40:
        total += 50
        range39 += 1
    elif 39 < result < 51:
        total += 100
        range50 += 1

print(f'{total:.2f}')
print(f'From 0 to 9: {range9 / rounds * 100:.2f}%')
print(f'From 10 to 19: {range19 / rounds * 100:.2f}%')
print(f'From 20 to 29: {range29 / rounds * 100:.2f}%')
print(f'From 30 to 39: {range39 / rounds * 100:.2f}%')
print(f'From 40 to 50: {range50 / rounds * 100:.2f}%')
print(f'Invalid numbers: {invalid / rounds * 100:.2f}%')
