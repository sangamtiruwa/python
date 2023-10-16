'''2. Write a program that asks the user to enter numbers until they input an empty string to quit.
At the end, the program prints out the five greatest numbers sorted in descending order. Hint: You can reverse
the order of sorted list items by using the sort method with the reverse=True argument.'''

numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if numbers:
    sorted_numbers = sorted(numbers, reverse=True)[:5]

    print("The five greatest numbers in descending order:")
    for num in sorted_numbers:
        print(num)
else:
    print("No numbers were entered.")
