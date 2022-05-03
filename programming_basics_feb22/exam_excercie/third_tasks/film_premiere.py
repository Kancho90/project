movie_name = input()
package = input()
number_of_tickets = int(input())

price = 1
if movie_name == 'John Wick':
    if package == 'Drink':
        price = 12
    elif package == 'Popcorn':
        price = 15
    elif package == 'Menu':
        price = 19
elif movie_name == 'Star Wars':
    if package == 'Drink':
        price = 18
    elif package == 'Popcorn':
        price = 25
    elif package == 'Menu':
        price = 30
elif movie_name == 'Jumanji':
    if package == 'Drink':
        price = 9
    elif package == 'Popcorn':
        price = 11
    elif package == 'Menu':
        price = 14

total = price * number_of_tickets
if movie_name == 'Star Wars' and number_of_tickets >= 4:
    total = total * 0.7
elif movie_name == 'Jumanji' and number_of_tickets == 2:
    total = total * 0.85

print(f'Your bill is {total:.2f} leva.')