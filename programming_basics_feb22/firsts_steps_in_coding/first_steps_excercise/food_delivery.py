chicken_order = int(input())
fish_menus = int(input())
veg_menus = int(input())
order_price = (chicken_order * 10.35) + (fish_menus * 12.40) + (veg_menus * 8.15)
order_total = (order_price * 0.2) + order_price + 2.5
print(order_total)
