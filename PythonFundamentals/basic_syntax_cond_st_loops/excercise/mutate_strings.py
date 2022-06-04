string1 = input()
string2 = input()

last_print = string1

for letter in range(len(string1)):
    left_part = string2[:letter + 1]
    right_part = string1[letter+1:]
    current_string = left_part + right_part
    if current_string == last_print:
        continue
    print(current_string)
    last_print = current_string