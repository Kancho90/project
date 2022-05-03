a = int(input())
end = int(input())
magic = int(input())
combination = 0
success = False

for x in range(a, end + 1):
    for y in range(a, end + 1):
        result = x + y
        combination += 1
        if result == magic:
            success = True
            break
    if success:
        break


if success:
    print(f'Combination N:{combination} ({x} + {y} = {magic})')
else:
    print(f'{combination} combinations - neither equals {magic}')