name = input()
days = int(input())
tickets = int(input())
price = float(input())
cut = int(input())

per_day = price * tickets
total = per_day * days
cut = 1 - (cut / 100)
total_final = total * cut

print(f'The profit from the movie {name } is {total_final:.2f} lv.')