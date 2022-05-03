egg_size =  input()
color = input()
number_of_eggs =  int(input())

price = 1

if egg_size == 'Large':
    if color == 'Yellow':
        price = 9
    elif color ==  'Red':
        price = 16
    elif color == 'Green':
        price = 12
elif  egg_size == 'Medium':
    if color == 'Yellow':
        price = 7
    elif color ==  'Red':
        price = 13
    elif color == 'Green':
        price = 9
elif egg_size  == 'Small':
    if color == 'Yellow':
        price = 5
    elif color ==  'Red':
        price = 9
    elif color == 'Green':
        price = 8

total = price *  number_of_eggs
profit = total *  0.65
print(f'{profit:.2f} leva.')

