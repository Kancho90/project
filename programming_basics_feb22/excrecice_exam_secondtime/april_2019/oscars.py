movie_name = input()
ticket_type = input()
number_of_tickets = int(input())

price = 1

if movie_name == 'A Star Is Born':
    if ticket_type == 'normal':
        price = 7.5
    elif ticket_type == 'luxury':
        price = 10.5
    elif ticket_type == 'ultra luxury':
        price = 13.5
elif movie_name == 'Bohemian Rhapsody':
    if ticket_type == 'normal':
        price = 7.35
    elif ticket_type == 'luxury':
        price = 9.45
    elif ticket_type == 'ultra luxury':
        price = 12.75
elif movie_name == 'Green Book':
    if ticket_type == 'normal':
        price = 8.15
    elif ticket_type == 'luxury':
        price = 10.25
    elif ticket_type == 'ultra luxury':
        price = 13.25
elif movie_name == 'The Favourite':
    if ticket_type == 'normal':
        price = 8.75
    elif ticket_type == 'luxury':
        price = 11.55
    elif ticket_type == 'ultra luxury':
        price = 13.95

total = price * number_of_tickets
print(f'{movie_name} -> {total:.2f} lv.')