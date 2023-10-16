'''1. Write a program that asks a fisher the length of a zander in centimeters. If the zander does
not fulfill the size limit, the program instructs to release the fish back into the lake and notifies the
user of how many centimeters below the size limit the caught fish was. A zander must be 42 centimeters or
longer to meet the size limit.'''


Zander = float(input("What is the length of the Zander in centimeters?: "))
if Zander >= 45:
    print("It is perfect size, You can take it.")
else:
    print("Invalid size, release to the water.")