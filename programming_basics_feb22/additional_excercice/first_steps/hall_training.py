w = float(input())
h = float(input())
h_reduced = (h * 100) - 100

desks_h = h_reduced // 70
desks_w = w * 100 // 120
total = desks_h * desks_w - 3


print(total)