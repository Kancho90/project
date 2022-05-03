lenght_cm = int(input())
width_cm = int(input())
hight_cm = int(input())
percentage = float(input())

volume = lenght_cm * width_cm * hight_cm
volume_l = volume / 1000
volume_end = (1 - (percentage/100)) *volume_l

print(volume_end)
