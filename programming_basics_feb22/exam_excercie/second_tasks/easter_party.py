number_of_guests = int(input())
price_per_guest = float(input())
budget = float(input())

discount_price = price_per_guest
if number_of_guests > 20:
    discount_price = price_per_guest * 0.75
elif 10 <= number_of_guests <= 15:
    discount_price = price_per_guest * 0.85
elif 15 < number_of_guests <= 20:
    discount_price = price_per_guest * 0.8

total_price = discount_price * number_of_guests + (budget * 0.1)
if budget >= total_price:
    money_left = budget - total_price
    print(f'It is party time! {money_left:.2f} leva left.')
else:
    money_needed = total_price - budget
    print(f'No party! {money_needed:.2f} leva needed.')