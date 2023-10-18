'''2. Write a program that asks the user to enter names until he/she enters an empty string. After
each name is read the program either prints out New name or Existing name depending on whether the name was
entered for the first time. Finally, the program lists out the input names one by one, one below another in any order.
Use the set data structure to store the names.'''

name_set = set()

input_names = []

while True:
    name = input("Enter a name (or press Enter to finish): ")

    if name == "":
        break

    if name in name_set:
        print("Existing name")
    else:
        print("New name")
        name_set.add(name)

    input_names.append(name)

print("\nList of input names:")
for name in input_names:
    print(name)
