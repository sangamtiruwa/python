'''4. Write a game where the computer draws a random integer between 1 and 10. The user tries to
guess the number until they guess the right number. After each guess the program prints out a text: Too high,
 Too low or Correct. Notice that the computer must not change the number between guesses.'''

import random

target_number = random.randint(1,10)

while True:
    user_guess = int(input("Guess the number between 1 and 10: "))

    if user_guess == target_number:
        print("Correct! You guessed the right number.")
        break
    elif user_guess < target_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

