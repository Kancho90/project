h = float(input())
w = float(input())

w_reduced = (w * 100) - 100
desks_in_w = w_reduced // 70
desks_in_h = (h * 100) // 120

total_desks =  desks_in_h * desks_in_w - 3

print(total_desks)

