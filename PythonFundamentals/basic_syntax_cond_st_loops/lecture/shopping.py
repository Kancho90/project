budget = int(input())

item = input()

while True:
    if item == 'End':
        print(f'You bought everything needed.')
        break
    budget -= int(item)

    if budget < 0:
        print(f'You went in overdraft!')
        break

    item = input()