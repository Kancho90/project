weight = float(input())
type = input()
distance = int(input())
price = 0

if type == 'standard':
    if weight < 1:
        price = distance * 0.03
    elif 1 <= weight < 10:
        price = distance * 0.05
    elif 10 <= weight < 40:
        price = distance * 0.10
    elif 40 <= weight < 90:
        price = distance * 0.15
    else:
        price = distance * 0.2
elif type == 'express':
    if weight < 1:
        price = (distance * 0.03) + (0.8 * 0.03 * distance * weight)
    elif 1 <= weight < 10:
        price = (distance * 0.05) + (0.4 * 0.05 * distance * weight)
    elif 10 <= weight < 40:
        price = (distance * 0.10) + (0.05 * 0.1 * distance * weight)
    elif 40 <= weight < 90:
        price = (distance * 0.15) + (0.02 * 0.15 * distance * weight)
    else:
        price = (distance * 0.2 ) + (0.01 * 0.2 * distance * weight)

print(f'The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.')