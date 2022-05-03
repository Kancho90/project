eggs = int(input())

eggs_sold = 0
total_eggs = eggs

while True:
    command = input()

    if command == 'Close':
        print('Store is closed!')
        print(f'{eggs_sold} eggs sold.')
        break
    number = int(input())
    if command == 'Buy':
        if number > total_eggs:
            print('Not enough eggs in store!')
            print(f'You can buy only {total_eggs}.')
            break
        total_eggs -= number
        eggs_sold += number
    elif command == 'Fill':
        total_eggs += number
