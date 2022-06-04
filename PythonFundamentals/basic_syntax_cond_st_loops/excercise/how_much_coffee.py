event = input()

coffees_needed = 0
list = ["dog", "cat", "movie", "coding"]
while event != "END":
    if event.lower() in list:
        if event.isupper():
            coffees_needed += 2
        else:
            coffees_needed += 1
    event = input()

if coffees_needed > 5:
    print('You need extra sleep')
else:
    print(coffees_needed)