budget = float(input())
videocards = int(input())
processors  = int(input())
ram_sticks = int(input())

price_videocards = 250
total_videocards = videocards * price_videocards
price_processors = total_videocards * 0.35
price_ram = total_videocards * 0.1
total_processors = processors * price_processors
total_ram = ram_sticks * price_ram

total_price = total_videocards + total_processors + total_ram
if videocards > processors:
    total_price = total_price * 0.85


money = budget - total_price
money_needed = total_price - budget

if money >= 0:
    print(f'You have {money:.2f} leva left!')
elif money < 0:
    print(f'Not enough money! You need {money_needed:.2f} leva more!')

