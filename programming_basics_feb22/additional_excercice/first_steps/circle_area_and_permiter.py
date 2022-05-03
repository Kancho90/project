from math import pi

r = float(input())

area = pi * r * r
calculated_area = "{:.2f}".format(area)

perimeter = 2 * pi *  r
calculated_perimeter = "{:.2f}".format(perimeter)


print(calculated_area)
print(calculated_perimeter)