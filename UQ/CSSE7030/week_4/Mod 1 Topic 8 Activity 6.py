def modify(xs):
    """ Function that takes in a list of strings, xs, and returns a
        a new list consisting of concatenated adjacent strings.

    Parameters:
        xs: The list of strings

    Return:
        list: a new list of concatenated adjacent strings.

    """

    result = []

    length = len(xs)
    i = 0

    while i < length - 1:
        result.append(xs[i]+xs[i+1])
        i += 2
    
    if i == length - 1:
        #this happens if there is one more string in xs left to be added to new list
        result.append(xs[i])

    return result
