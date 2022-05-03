import sys
import math
kozunaci = int(input())

total_sugar = 0
total_flour = 0
max_sugar = -sys.maxsize
max_flour = -sys.maxsize

for i in range(kozunaci):
    sugar = int(input())
    total_sugar += sugar
    if sugar > max_sugar:
        max_sugar = sugar
    flour = int(input())
    total_flour += flour
    if flour > max_flour:
        max_flour = flour

packets_sugar = math.ceil(total_sugar / 950)
packets_flour = math.ceil(total_flour / 750)

print(f'Sugar: {packets_sugar}')
print(f'Flour: {packets_flour}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')