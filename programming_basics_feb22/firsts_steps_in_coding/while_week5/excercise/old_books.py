favourite_book = input()
books_searched = 0

book = input()

while True:
    if book == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {books_searched} books.')
        break
    if book == favourite_book:
       print(f'You checked {books_searched} books and found it.')
       break

    books_searched += 1
    book = input()