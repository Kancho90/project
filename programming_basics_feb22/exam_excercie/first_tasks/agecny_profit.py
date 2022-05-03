company_name = input()
tickets_adults = int(input())
tickets_kids = int(input())
price_adults = float(input())
tax = float(input())
price_kids = price_adults * 0.3

total_adults = tickets_adults * (price_adults + tax)
total_kids = tickets_kids * (price_kids + tax)
total_profit = (total_kids + total_adults) * 0.2
formatted_profit = "{:.2f}".format(total_profit)


print (f'The profit of your agency from {company_name} tickets is {formatted_profit} lv.')