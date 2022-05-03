import math

price_racket = float(input())
number_of_rackets = int(input())
pair_of_shoes = int(input())

price_of_shoes = price_racket / 6
total = (price_of_shoes * pair_of_shoes) + (price_racket * number_of_rackets)
extra = total * 0.2
total_extra = total + extra
djokovich = math.floor(total_extra / 8)
sponsors_price = total_extra * 7 / 8
sponrs = math.ceil(sponsors_price)

print(f'Price to be paid by Djokovic {djokovich}')
print(f'Price to be paid by sponsors {sponrs}')