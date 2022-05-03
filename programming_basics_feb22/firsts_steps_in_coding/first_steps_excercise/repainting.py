nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours = int(input())
nylon_total = (nylon_needed + 2) * 1.5
paint_total = paint_needed  *  1.1 * 14.5
thinner_total = thinner_needed  * 5
total_price = nylon_total + paint_total + thinner_total + 0.4
total_price_with_labor = total_price + ((total_price * 0.3)* hours)
print(total_price_with_labor)

