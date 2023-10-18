'''4. Write a function that gets a list of integers as a parameter. The function returns the sum of all
the numbers in the list. For testing, write a main program where you create a list, call the function, and
print out the value it returned.'''


def sum_of_list(numbers):
    total = sum(numbers)
    return total

integer_list = [1, 2, 3, 4, 5]

result = sum_of_list(integer_list)

print(f"The sum of the list is: {result}")
