rent = int(input())

price_statues = rent * 0.7
price_catering = price_statues * 0.85
price_sound = price_catering * 0.5

total = rent + price_sound + price_statues + price_catering
print(f'{total:.2f}')