from termcolor import colored,cprint

name = 'Честита Баба Марта!'
k = name[0:6]
x = ''

for j in name:
    if x == k:
        cprint(name, 'red')
        break
    else:
        x += j
        cprint(x, 'red')

