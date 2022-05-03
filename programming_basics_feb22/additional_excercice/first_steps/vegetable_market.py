price_vegetables_kg = float(input())
price_fruits_kg = float(input())
vegetables = int(input())
fruits = int(input())

total_vegetables = price_vegetables_kg * vegetables
total_fruits = price_fruits_kg * fruits
total = total_vegetables +  total_fruits
total_eur = total / 1.94

formatted_total = '{:.2f}'.format(total_eur)

print(formatted_total)