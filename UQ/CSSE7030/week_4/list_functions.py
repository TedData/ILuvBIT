
def double(xs):
    """Return the list of the doubles of the elems of xs

    ...
    """
    result = []
    for x in xs:
        result.append(2*x)
    return result

def evens(xs):
    """Return the even elems of xs

    ...
    """
    result = []
    for i,x in enumerate(xs):
        if i % 2 == 0:
            result.append(x)
    return result

