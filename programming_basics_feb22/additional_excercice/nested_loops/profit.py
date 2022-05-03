lv1 = int(input())
lv2 = int(input())
lv5 = int(input())
r = int(input())

sum = 0
for i in range(0, lv1 + 1):
    for i2 in range(0, lv2 + 1):
        for i3 in range(0, lv5+ 1):
            sum = i * 1 + i2 * 2 + i3 * 5
            if sum == r:
                print(f'{i} * 1 lv. + {i2} * 2 lv. + {i3} * 5 lv. = {r} lv.')