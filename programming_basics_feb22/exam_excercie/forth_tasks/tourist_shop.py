budget = float(input())

remaining_money = budget
number_of_products = 0
product_price = 0

while True:
    name = input()
    if name == 'Stop':
        break

    price = float(input())
    number_of_products += 1
    if number_of_products % 3 == 0:
        price /= 2
    remaining_money -= price
    product_price += price

    if remaining_money < 0:
        number_of_products -= 1
        break




if remaining_money >= 0:
    print(f'You bought {number_of_products} products for {product_price:.2f} leva.')
else:
    print(f"You don't have enough money!")
    print(f'You need {abs(remaining_money):.2f} leva!')