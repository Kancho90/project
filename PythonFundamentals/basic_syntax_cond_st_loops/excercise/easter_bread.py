budget = float(input())
flour_price = float(input())
price_eggs = flour_price * 0.75
price_milk = (flour_price * 1.25) / 4

loafs = 0
eggs = 0

total_spent = 0

while True:
    if budget <= total_spent + flour_price + price_eggs + price_milk:
        break
    total_spent += flour_price + price_eggs + price_milk
    loafs += 1
    eggs += 3
    if loafs % 3 == 0:
        eggs -= loafs - 2



left = budget - total_spent

print(f'You made {loafs} loaves of Easter bread! Now you have {eggs} eggs and {left:.2f}BGN left.')