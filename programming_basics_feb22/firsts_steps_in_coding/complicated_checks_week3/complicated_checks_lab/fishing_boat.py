budget = int(input())
season = input()
fishermen = int(input())

price = 0
if season == "Spring":
    price = 3000
elif season == 'Summer' or season == "Autumn":
    price = 4200
elif season == 'Winter':
    price = 2600

if fishermen <= 6:
    price = price * 0.9
elif 6 < fishermen <= 11:
    price = price * 0.85
else:
    price = price * 0.75
additional_discount = ['Summer', 'Spring', 'Winter']
if (fishermen % 2) == 0 and season in additional_discount:
    price = price * 0.95

money =  abs(budget - price)
if budget >= price:
    print(f'Yes! You have {money:.2f} leva left.')
else:
    print(f'Not enough money! You need {money:.2f} leva.')