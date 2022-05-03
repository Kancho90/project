import random
from string import digits, punctuation, ascii_lowercase, ascii_uppercase

all_combination_from_digits_lettres_symbols = digits + punctuation + ascii_lowercase + ascii_uppercase

password_length = int(input('Enter the password length: '))

password = ''.join(random.sample(all_combination_from_digits_lettres_symbols, password_length))
print(f'Your password is: {password}')