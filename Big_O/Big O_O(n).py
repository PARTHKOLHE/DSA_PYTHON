'''
Questions: Implement a Python function called print_items.
This function should take a single integer as an argument and print out a sequence of numbers from 0 up to, but not including, the provided integer.
The function should use a for loop and Python's built-in range function to generate the sequence of numbers.
The function signature should be: def print_items(n):
'''
# Answer:
def print_items(n):
    for items in range(0,n):
        print (items)
            
# DO NOT CHANGE THIS LINE:
print_items(10)