'''3. Write a function that gets the quantity of gasoline in American gallons and returns the number
converted to litres. Write a main program that asks for a volume in gallons from the user and converts the value
to liters. The conversion must be done by using the function. Conversions continue until the user inputs a negative value.'''


def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters


while True:
    gallons = float(input("Enter a volume in American gallons (negative value to quit): "))

    if gallons < 0:
        break

    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons is equivalent to {liters:.2f} liters.")

print("Program terminated.")

