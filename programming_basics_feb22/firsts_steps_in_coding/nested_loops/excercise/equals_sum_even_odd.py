num1 = int(input())
num2 =  int(input())

for number in range(num1, num2 + 1):
    even_sum = 0
    odd_sum = 0
    for current in range(len(str(number))):
        if current % 2  == 0:
            even_sum += int(str(number)[current])
        else:
            odd_sum += int(str(number)[current])
    if even_sum == odd_sum:
        print(f'{number}', end = ' ')