kozunaci = int(input())
egg_cartons = int(input())
cookies = int(input())

price_kozunaci = kozunaci * 3.2
price_eggs = egg_cartons * 4.35
price_cookies = cookies * 5.4
price_paint = (egg_cartons * 12) * 0.15

total = price_paint + price_eggs + price_cookies + price_kozunaci
formatted = '{:.2f}'.format(total)

print(formatted)
