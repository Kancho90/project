n = int(input())
total = 0

for i in range(n):
    price = float(input())
    days = int(input())
    capsulse_needed = int(input())
    if capsulse_needed < 1 or capsulse_needed > 2000:
        continue
    elif price < 0.01 or price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    total_order = capsulse_needed * days * price
    total += total_order
    print(f'The price for the coffee is: ${total_order:.2f}')

print(f'Total: ${total:.2f}')
