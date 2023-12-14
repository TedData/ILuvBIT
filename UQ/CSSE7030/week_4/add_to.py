def add_to(existing_list, num):
    """Adds numbers 0 to 'num' to the end of the 'existing_list'.

    Parameters:
        existing_list (list): The list to which numbers will be added.
        num (int): The number up to which will be added to 'existing_list'.
        
    Examples:
        >>> a_list = []
        >>> add_to(a_list, 4)
        >>> a_list
        [0, 1, 2, 3]
    """
    for i in range(num):
        existing_list.append(i)


# If this module is run the code below will execute.
# It imports the doctest module and runs the tests found in the factorise
# function's docstring, under the Examples: heading.
# If the tests pass nothing is output.
# If any tests fail an error message will be output for each failure.
# You can execute the code from the command-line in verbose mode to see the
# output of the test executions.
#     python add_to.py -v

if __name__ == "__main__" :
    import doctest
    doctest.testmod()

# Example use
a_list = [3, 5, 6, 87, 1, 5]
add_to(a_list, 5)
print(a_list)
