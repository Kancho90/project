city_name = input()
equipment_type = input()
vip_option = input()
days_to_stay = int(input())
price = 0
if days_to_stay > 7:
    days_to_stay -= 1
if days_to_stay < 1:
    print('Days must be positive number!')
elif city_name not in 'Bansko Borovets Varna Burgas' \
        or equipment_type not in 'withEquipment noEquipment withBreakfast noBreakfast':
    print('Invalid input!')
elif city_name == 'Bansko' or city_name == 'Borovets':

    if equipment_type == 'withEquipment':
        price = days_to_stay * 100
        if vip_option == 'yes':
            price -= price * 0.10
    elif equipment_type == 'noEquipment':
        price = days_to_stay * 80
        if vip_option == 'yes':
            price -= price * 0.05
    print(f'The price is {price:.2f}lv! Have a nice time!')
elif city_name == 'Varna' or city_name == 'Burgas':
    if equipment_type == 'withBreakfast':
        price = days_to_stay * 130
        if vip_option == 'yes':
            price -= price * 0.12
    elif equipment_type == 'noBreakfast':
        price = days_to_stay * 100
        if vip_option == 'yes':
            price -= price * 0.07
    print(f'The price is {price:.2f}lv! Have a nice time!')
