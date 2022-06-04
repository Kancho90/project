string = input()

for index, letter in string:
    if letter.isupper:
        print(index,end='')