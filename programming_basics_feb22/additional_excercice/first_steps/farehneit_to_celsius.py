degrees_celsius = float(input())
degrees_farenheit = (degrees_celsius * 1.8) + 32

formatted_farenheit = "{:.2f}".format(degrees_farenheit)

print(formatted_farenheit)