import math

number_of_people = int(input())
entry_fee = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

price_entry = number_of_people * entry_fee
sunbeds_required = number_of_people * 0.75
people_sunbed = math.ceil(sunbeds_required)
price_sunbed = people_sunbed * sunbed_price
number_of_people_for_umbrella_request = (number_of_people / 2)
number_of_people_for_umbrella = math.ceil(number_of_people_for_umbrella_request)
price_umbrella = number_of_people_for_umbrella * umbrella_price

total = price_umbrella + price_entry + price_sunbed
result = "{:.2f}".format(total)

print(f'{result} lv.')