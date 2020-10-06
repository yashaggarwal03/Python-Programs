# Program to extract a list of numbers that are multiples of 5 from a list of integers using filter function in python.
# The filter function takes two arguments,
# a function object and an iterable like list, tuple,etc.
# The function object passed should return either true or false.

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

list_answer = list(filter(lambda x:x%5 == 0, input_list))

print(list_answer)

# Output: [5, 10, 15]
