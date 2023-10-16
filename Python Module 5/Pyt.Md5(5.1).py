'''1. Write a program that asks the user how many dice to roll. The program rolls all the dice once
 and prints out the sum of the numbers. Use a for loop.'''

import random

num_dice = int(input("How many dice to roll: "))

total_sum = 0

for _ in range(num_dice):
    roll = random.randint(1, 6)
    total_sum += roll

print(f"Sum of the dice rolls: {total_sum}")

