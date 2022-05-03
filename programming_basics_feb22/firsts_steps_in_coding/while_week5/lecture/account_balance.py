total = 0
add = input()

while add != 'NoMoreMoney':
    current = float(add)

    if float(current) < 0:
        print('Invalid operation!')
        break

    total += current
    print(f'Increase: {float(add):.2f}')
    add = input()

print(f'Total: {total:.2f}')