number_of_pages = int(input())
pages_per_hour = int(input())
days_to_read = int(input())
hours_needed = (number_of_pages // pages_per_hour) // days_to_read
print(hours_needed)
