'''2. Modify the function above so that it gets the number of sides on the dice as a parameter.
With the modified function you can for example roll a 21-sided role-playing dice. The difference to the last
exercise is that the dice rolling in the main program continues until the program gets the maximum number on
the dice, which is asked from the user at the beginning.'''

import random

def roll_dice(sides):
    return random.randint(1, sides)

max_number = int(input("Enter the maximum number on the dice: "))

rolls = 0
while True:
    result = roll_dice(max_number)
    rolls +=1
    print(f"Roll {rolls}: {result}")
    if result == max_number:
        break

print(f"It took {rolls} rolls to get the maximum number ({max_number}) on the dice.")
