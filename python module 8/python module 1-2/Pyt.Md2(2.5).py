#5. Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and outputs the result to the user:

#One talent is 20 pounds.
#One pound is 32 lots.
#One lot is 13,3 grams.

talents = float(input("Enter the mass in talents: "))
pounds = float(input("Enter the mass in pounds: "))
lots = float(input("Enter the mass in lots: "))
pounds_per_talent = 20
lots_per_pound = 32
grams_per_lot = 13.3
total_grams = (talents * pounds_per_talent + pounds) * lots_per_pound * grams_per_lot
kilograms = total_grams // 1000
grams = total_grams % 1000
print(f"The mass is approximately {kilograms} kilograms and {grams} grams.")