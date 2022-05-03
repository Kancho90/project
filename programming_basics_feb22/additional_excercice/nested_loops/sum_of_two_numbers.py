n1 = int(input())
n2 = int(input())
magic_number = int(input())

combinations = 0
success = False

for i in range(n1, n2 + 1):
    for i2 in range(n1, n2 + 1):
        combinations += 1
        if i + i2 == magic_number:
            success = True
            break
    if i + i2 == magic_number:
        break

if success:
    print(f'Combination N:{combinations} ({i} + {i2} = {magic_number})')
elif not success:
    print(f'{combinations} combinations - neither equals {magic_number}')
