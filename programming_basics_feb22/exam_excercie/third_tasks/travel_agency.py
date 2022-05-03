city = input()
package_type = input()
vip_discount = input()
days_of_stay = int(input())

cities = ['Bansko', 'Borovets', 'Varna', 'Burgas']
packages = ['noEquipment', "withEquipment", "noBreakfast","withBreakfast"]

price = 1
if days_of_stay > 7:
    days_of_stay -= 1

if days_of_stay < 1:
    print('Days must be positive number!')
elif city not in cities or package_type not in packages:
    print('Invalid input!')
else:
    if city in ['Bansko', 'Borovets']:
        if package_type == 'noEquipment':
            price = 80
            if vip_discount == 'yes':
                price = price * 0.95
        elif package_type == 'withEquipment':
            price = 100
            if vip_discount == 'yes':
                price = price * 0.9
    elif city in ['Burgas', 'Varna']:
        if package_type == 'noBreakfast':
            price = 100
            if vip_discount == 'yes':
                price = price * 0.93
        elif package_type == 'withBreakfast':
            price = 130
            if vip_discount == 'yes':
                price = price * 0.88
    total = price * days_of_stay
    print(f'The price is {total:.2f}lv! Have a nice time!')

