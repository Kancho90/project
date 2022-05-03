month =  input()
number_of_days = int(input())

price_studio = 1
price_app = 1

if month == 'May' or month == 'October':
    price_studio = 50
    price_app = 65
    if 7 < number_of_days <= 14:
        price_studio = price_studio * 0.95
    elif number_of_days > 14:
        price_studio = price_studio * 0.7
elif month == 'June' or month == 'September':
    price_studio = 75.2
    price_app = 68.7
    if number_of_days > 14:
        price_studio = price_studio * 0.8
elif month == 'July' or month == 'August':
    price_studio = 76
    price_app = 77

if number_of_days > 14:
    price_app = price_app * 0.9

total_studio = price_studio * number_of_days
total_app = price_app * number_of_days

print(f'Apartment: {total_app:.2f} lv.')
print(f'Studio: {total_studio:.2f} lv.')