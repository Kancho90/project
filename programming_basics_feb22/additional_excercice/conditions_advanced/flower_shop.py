hristantemi_number = int(input())
roses_number = int(input())
tuplis_number = int(input())
season = input()
holiday = input()

total = 1

if season == 'Spring' or season == 'Summer':
    total = roses_number * 4.1 + hristantemi_number * 2 + 2.5 * tuplis_number
    if holiday == 'Y':
        total = total * 1.15
    if season == 'Spring' and tuplis_number > 7:
        total = total * 0.95

if season == 'Autumn' or season == 'Winter':
    total = roses_number * 4.5 + hristantemi_number * 3.75 + 4.15 * tuplis_number
    if holiday == 'Y':
        total = total * 1.15
    if season == 'Winter' and roses_number >= 10:
            total = total * 0.9

if roses_number + tuplis_number + hristantemi_number > 20:
    total = total * 0.8

end_total = total + 2
print(f'{end_total:.2f}')