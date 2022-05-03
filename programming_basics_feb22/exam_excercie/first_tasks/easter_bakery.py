price_flour = float(input())
flour_kg = float(input())
sugar_kg = float(input())
egg_cartons = int(input())
maq_packages = int(input())

price_sugar = price_flour * 0.75
price_eggs = price_flour * 1.1
price_maq = price_sugar * 0.2

total_sugar = price_sugar * sugar_kg
total_eggs = price_eggs * egg_cartons
total_maq = price_maq * maq_packages
total_flour = flour_kg * price_flour

total_price = total_maq + total_flour + total_eggs + total_sugar
total = '{:.2f}'.format(total_price)

print(total)