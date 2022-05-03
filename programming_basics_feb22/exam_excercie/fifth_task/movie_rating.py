import sys

movies = int(input())

highest = -sys.maxsize
highest_name = ''
lowest = sys.maxsize
lowest_name = ''
total = 0


for i in range(movies):
    name = input()
    rating = float(input())
    total += rating
    if rating > highest:
        highest = rating
        highest_name = name
    if rating < lowest:
        lowest = rating
        lowest_name = name

print(f'{highest_name} is with highest rating: {highest:.1f}')
print(f'{lowest_name} is with lowest rating: {lowest:.1f}')
print(f'Average rating: {total / movies:.1f}')