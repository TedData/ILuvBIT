def sumto(n):
    """Return the sum of numbers from 1 to n"""

    total = 0
    m = 1
    while m <= n:
        total = total + m  # total += m is a shorthand
        m += 1
    return total

def prodto(n):
    """ Return the product of numbers from 1 to n"""

    product=1
    m=1
    while m<=n:
        product=product*m
        m+=1
    return product
