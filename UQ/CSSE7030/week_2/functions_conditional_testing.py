def add(n, m):
    """Return the result of adding n and m"""

    return n+m

def add2(n,m):
    """Return the result of adding n and m

    add2(int,int) => int

    Parameters:
        n (int): the first integer to be added
        m (int): the second integer to be added
    """

    print(n+m)


def size(n):
    """Return 'One', 'Two, or 'Many' depending on n"""

    if n == 1:
        result = "One"
    elif n ==2:
        result = "Two"
    else:
        result = "Many"
    return result
    

def sumto2(n):
    """Return the sum of numbers from 1 to n using a for loop"""

    total = 0
    for m in range(1,n+1):
        total = total + m  # total += m is a shorthand
    return total
