bottles = int(input())

detergent = bottles * 750
used = 0
chinii = 0
tendjeri = 0
cycles = 0

while detergent >= used:
    washed = input()

    if washed == 'End':
        break

    cycles += 1

    if cycles % 3 == 0:
        tendjeri += int(washed)
        used += (int(washed)* 15)
    else:
        chinii += int(washed)
        used += (int(washed) * 5)

diff = abs(detergent - used)
if detergent >= used:
    print(f'Detergent was enough!')
    print(f'{chinii} dishes and {tendjeri} pots were washed.')
    print(f'Leftover detergent {diff} ml.')
else:
    print(f'Not enough detergent, {diff} ml. more necessary!')