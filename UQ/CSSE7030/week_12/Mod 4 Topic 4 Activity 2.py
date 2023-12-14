import random

def stringshuffle(xs):
    """ Randomise the characters in a string """
    ys =[(random.random(),x) for x in xs]
    ys.sort()
    lst = [x for y,x in ys]
    return "".join(lst)
