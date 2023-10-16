'''2. Write a program that converts inches to centimeters until the user inputs a negative value.
Then the program ends.'''

inches_to_cm = 2.54

while True:
    inches = float(input("Enter a value in inches or a negative value to quit: "))

    if inches < 9:
        print("program ended.")
        break

    centimeters = inches * inches_to_cm
    print(f"{inches} inches is equal to {centimeters} centimeters.")