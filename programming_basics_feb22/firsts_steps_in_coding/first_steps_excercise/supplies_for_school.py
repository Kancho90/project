pens = int(input())
total_pens = pens * 5.8

markers = int(input())
total_markers = markers * 7.2

cleaning = int(input())
total_cleaning = cleaning * 1.2


discount = int(input())
discount_percentage = discount / 100

total_price = (total_pens + total_markers + total_cleaning) - \
              (total_pens + total_markers + total_cleaning)* discount_percentage

print(total_price)
