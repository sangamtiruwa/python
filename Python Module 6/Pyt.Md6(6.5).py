'''5. Write a function that gets a list of integers as a parameter. The function returns a second list that
is otherwise the same as the original list except that all uneven numbers have been removed. For testing, write
a main program where you create a list, call the function, and then print out both the original as well as the cut-down list.'''


def remove_odd_numbers(input_list):
    even_numbers = [x for x in input_list if x % 2 == 0]
    return even_numbers

integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_list = remove_odd_numbers(integer_list)

print("Original list:", integer_list)

print("Cut-down list (even numbers only):", even_list)
