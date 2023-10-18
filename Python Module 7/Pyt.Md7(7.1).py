'''1. Write a program that asks the user for a number of a month and then prints out the corresponding
season (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can
define each season to last three months, December being the first month of winter.'''


seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter the number of a month (1-12): "))

if 1 <= month <= 12:
    season_index = (month - 1) // 3
    season = seasons[season_index]
    print(f"The corresponding season for month {month} is {season}.")
else:
    print("Invalid input. Please enter a month number between 1 and 12.")
