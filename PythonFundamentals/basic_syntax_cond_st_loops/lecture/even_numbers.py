number = int(input())

for i in range(number):
    m = int(input())
    if m % 2 != 0:
        print(f"{m} is odd!")
        break

else:
    print("All numbers are even.")