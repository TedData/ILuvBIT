def odd_symmetric(lst):
    if len(lst) == 1:
        #original list had odd number of elements, so cannot
        #be odd symmetric
        return False
    if len(lst) == 0:
        return True
    if (lst[0] == -lst[-1]):
        #if the first element in the list is
        #the the same as the negative of the last
        #element in the list
        return odd_symmetric(lst[1:-1])
    #only get here if list is not odd symmetric
    return False
