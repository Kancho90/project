a = int(input())
b = int(input())
max_passwords = int(input())
generated_pass = 0
p1 = 35
p2 = 64
for x in range (1, a + 1):
    for y in range (1,b + 1):

        print(f'{chr(p1)}{chr(p2)}{x}{y}{chr(p2)}{chr(p1)}|', end='')
        generated_pass += 1
        p1 += 1
        if p1 > 55:
            p1 = 35
        p2 += 1
        if p2 > 96:
            p2 = 64
        if generated_pass == max_passwords:
            break
    if generated_pass == max_passwords:
        break

