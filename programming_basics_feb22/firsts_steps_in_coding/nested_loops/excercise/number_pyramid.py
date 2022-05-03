num = int(input())
condition = False
current_num = 1

for row in range (1, num + 1):
    for row2 in range(1, row + 1):
        if current_num > num:
            condition = True
            break
        print(f'{current_num}', end = ' ')
        current_num += 1
    if condition:
        break
    print()
