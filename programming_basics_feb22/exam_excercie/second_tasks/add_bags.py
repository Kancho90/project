price_20kg = float(input())
lugga_kg = float(input())
days_left = int(input())
number_of_luggage = int(input())

if lugga_kg > 20:
    actual_price = price_20kg
elif 10<= lugga_kg <= 20:
    actual_price = price_20kg * 0.5
else:
    actual_price = price_20kg * 0.2

if days_left > 30:
    day_price = actual_price * 1.1
elif 7 <= days_left <= 30:
    day_price = actual_price * 1.15
else:
    day_price = actual_price * 1.4

final_price = day_price * number_of_luggage
print(f'The total price of bags is: {final_price:.2f} lv.')