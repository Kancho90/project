strawberries_price = float(input())
bananas_in_kg = float(input())
oranges_in_kg = float(input())
raspberry_in_kg = float(input())
strawberries_in_kg = float(input())

price_raspberry = strawberries_price / 2
price_oranges = price_raspberry * 0.6
price_bananas = price_raspberry * 0.2

total = bananas_in_kg * price_bananas + strawberries_price * strawberries_in_kg + oranges_in_kg * price_oranges \
        + raspberry_in_kg * price_raspberry
total_sum = "{:.2f}".format(total)
print(total_sum)
