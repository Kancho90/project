x = float(input())
y = float(input())
h = float(input())

front_wall = (x * x) - (1.2 * 2)
back_wall = (x * x)
side_wall = (x * y) - (1.5 * 1.5)
total_walls = front_wall + back_wall + side_wall * 2
green_paint = total_walls / 3.4

green_paint_result = "{:.2f}".format(green_paint)

roof = 2 * x * y
roof_front = 2 * (x * h) / 2
roof_total = roof + roof_front
red_paint = roof_total / 4.3
red_paint_result = "{:.2f}".format(red_paint)

print(green_paint_result)
print(red_paint_result)
