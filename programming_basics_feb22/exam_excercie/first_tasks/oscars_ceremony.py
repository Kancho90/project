rent = int(input())

price_statues = rent * 0.7
price_catering = price_statues * 0.85
price_sound = price_catering / 2

total_price = rent + price_sound + price_statues + price_catering
formatted_price = "{:.2f}".format(total_price)

print(formatted_price)