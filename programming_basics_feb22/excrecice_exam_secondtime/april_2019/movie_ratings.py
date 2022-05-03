from sys import maxsize

number_of_movies = int(input())
total_rating = 0
max_rating = -maxsize
best_movie = ''
worst_rating = maxsize
worst_movie = ''

for m in range(1, number_of_movies + 1):
    name = input()
    rating = float(input())
    total_rating += rating
    if rating > max_rating:
        max_rating = rating
        best_movie = name
    elif rating < worst_rating:
        worst_movie = name
        worst_rating = rating

print(f'{best_movie} is with highest rating: {max_rating:.1f}')
print(f'{worst_movie} is with lowest rating: {worst_rating:.1f}')
print(f'Average rating: {total_rating / number_of_movies:.1f}')