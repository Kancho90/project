n = int(input())
washing_machine = float(input())
toy_price = int(input())
money = 0
gift = 0
number_of_toys = 0
stealing_brother = 0

for i in range (1, n + 1):
    if i % 2 == 0:
        gift += 10
        money += gift
        stealing_brother += 1
    else:
        number_of_toys += 1

total_lilly = money - stealing_brother + number_of_toys * toy_price
diff = abs(total_lilly - washing_machine)
if total_lilly >= washing_machine:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
