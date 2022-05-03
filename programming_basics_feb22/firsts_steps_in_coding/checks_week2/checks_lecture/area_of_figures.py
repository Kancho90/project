import math
figure = input()

if figure == "square":
    a = float(input())
    s = a * a
    print('{:.3f}'.format(s))
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    sr = a * b
    print('{:.3f}'.format(sr))
elif figure == "circle":
    r = float(input())
    s = math.pi * r * r
    print('{:.3f}'.format(s))
elif figure == "triangle":
    a = float(input())
    h = float(input())
    s = a * h /2
    print("{:.3f}".format(s))
