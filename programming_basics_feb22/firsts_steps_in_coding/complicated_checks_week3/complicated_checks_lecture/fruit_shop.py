fruit = input()
day = input()
quantity = float(input())

fruits_accepted =  ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']
days_accepted = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
price = 0

if fruit not in fruits_accepted or day not in days_accepted:
    print('error')
else:
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        if fruit == 'banana':
            price = 2.5
        elif fruit == 'apple':
            price = 1.2
        elif fruit == 'orange':
            price = 0.85
        elif fruit == 'grapefruit':
            price = 1.45
        elif fruit == 'kiwi':
            price = 2.7
        elif fruit == 'pineapple':
            price = 5.5
        elif fruit == 'grapes':
            price = 3.85
    elif day == 'Saturday' or day == 'Sunday':
        if fruit == 'banana':
            price = 2.7
        elif fruit == 'apple':
            price = 1.25
        elif fruit == 'orange':
            price = 0.9
        elif fruit == 'grapefruit':
            price = 1.6
        elif fruit == 'kiwi':
            price = 3
        elif fruit == 'pineapple':
            price = 5.6
        elif fruit == 'grapes':
            price = 4.2
    total = price * quantity
    print(f'{total:.2f}')



