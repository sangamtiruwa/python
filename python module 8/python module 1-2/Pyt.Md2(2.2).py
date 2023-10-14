#2. Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

radius = float(input("Enter the radius of the circle: "))
pi = 3.14159365359
area = pi*(radius**2)
print(f"The area of circle with the radius is {area: .2f}")