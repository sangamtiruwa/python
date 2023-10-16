'''3. Write a program that asks the user to enter numbers until they enter an empty string to quit.
Finally, the program prints out the smallest and largest number from the numbers it received'''

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
    smallest = min(numbers)
    largest = max(numbers)
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")
else:
    print("No numbers were entered.")
