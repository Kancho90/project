flower = input()
number_of_flowers = int(input())
budget = int(input())

price = 0
if flower == "Roses":
    price = 5
    if number_of_flowers > 80:
        price = price * 0.9
elif flower == 'Dahlias':
    price = 3.8
    if number_of_flowers > 90:
        price = price * 0.85
elif flower == "Tulips":
    price = 2.8
    if number_of_flowers > 80:
        price = price * 0.85
elif flower == 'Narcissus':
    price = 3
    if number_of_flowers < 120:
        price += price * 0.15
elif flower == 'Gladiolus':
    price = 2.5
    if number_of_flowers < 80:
        price += price * 0.20

total = price * number_of_flowers
remaining = abs(budget - total)
if budget >= total:
    print(f'Hey, you have a great garden with {number_of_flowers} {flower} and {remaining:.2f} leva left.')
else:
    print(f'Not enough money, you need {remaining:.2f} leva more.')
