'''6. Write a function that receives two parameters: the diameter of a round pizza in centimeters and the
price of the pizza in euros. The function calculates and returns the unit price of the pizza per square meter.
The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides
better value for money (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.'''


import math

def calculate_unit_price(diameter, price):
    radius = diameter / 2
    area_cm2 = math.pi * (radius ** 2)
    area_m2 = area_cm2 / 10000
    unit_price = price / area_m2
    return unit_price

print("Enter details for Pizza 1:")
diameter1 = float(input("Diameter (in centimeters): "))
price1 = float(input("Price (in euros): "))

print("\nEnter details for Pizza 2:")
diameter2 = float(input("Diameter (in centimeters): "))
price2 = float(input("Price (in euros): "))

unit_price1 = calculate_unit_price(diameter1, price1)
unit_price2 = calculate_unit_price(diameter2, price2)

print("\nUnit price for Pizza 1: {:.2f} euros per square meter".format(unit_price1))
print("Unit price for Pizza 2: {:.2f} euros per square meter".format(unit_price2))

if unit_price1 < unit_price2:
    print("Pizza 1 provides better value for money.")
elif unit_price2 < unit_price1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas have the same unit price.")
