fuel_type = input()
litres = float(input())
card = input()

price_gas = 0.93
price_diesel = 2.33
price_gasoline = 2.22

if card == "Yes":
    price_gas = price_gas - 0.08
    price_gasoline = price_gasoline - 0.18
    price_diesel = price_diesel - 0.12

price = 0
if fuel_type == "Gasoline":
    price = litres * price_gasoline
elif fuel_type == "Gas":
    price = litres * price_gas
else:
    price = litres * price_diesel

discounted_price = price
if 20 <= litres <= 25:
    discounted_price = price * 0.92
elif litres > 25:
    discounted_price = price * 0.9

print(f'{discounted_price:.2f} lv.')