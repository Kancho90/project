letter = input()
c = 0
o = 0
n = 0
word = ''
print_word = ''


while letter != 'End':
    if letter.isalpha():
        if letter == 'c' and c == 0:
            c += 1
            if c == 1 and o == 1 and n == 1:
                word += ' '
                c, o, n = 0, 0, 0
                print_word = word

        elif letter == 'o' and o == 0:
            o += 1
            if c == 1 and o == 1 and n == 1:
                word += ' '
                c, o, n = 0, 0, 0
                print_word = word
        elif letter == 'n' and n == 0:
            n += 1
            if c == 1 and o == 1 and n == 1:
                word += ' '
                c, o, n = 0, 0, 0
                print_word = word
        else:
            word += letter 


    letter = input()
print(print_word)