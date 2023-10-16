'''5. Write a program that asks the user for a username and password. If either or both are incorrect,
the program ask the user to enter the username and password again. This continues until the login information
is correct or wrong credentials have been entered five times. If the information is correct, the program prints
out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.'''

correct_username = "python"
correct_password = "rules"

attempts = 0

while attempts < 5:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Incorrect information. Please try again.")
        attempts += 1

if attempts == 5:
    print("Access denied. You've reached the maximum number of attempts.")

