import math

days = int(input())
total_food = float(input())

dog_eaten = 0
dog_cookie = 0
cat_eaten = 0
cat_cookie = 0

for i in range(1, days + 1):
    dog = int(input())
    cat = int(input())
    dog_eaten += dog
    cat_eaten += cat
    if i % 3 == 0:
        cat_cookie += cat * 0.1
        dog_cookie += dog * 0.1

total_cookies = int(cat_cookie + dog_cookie)
eaten = dog_eaten + cat_eaten
print(f'Total eaten biscuits: {total_cookies}gr.')
print(f'{eaten / total_food * 100:.2f}% of the food has been eaten.')
print(f'{dog_eaten / eaten * 100:.2f}% eaten from the dog.')
print(f'{cat_eaten /eaten * 100:.2f}% eaten from the cat.')