"""
Support for testing for, and finding primes.

"""

import math

##def is_prime(num) :
##    """Returns True iff 'num' is prime.
##
##    Parameters:
##        num (int): Integer value to be tested to see if it is prime.
##
##    Return:
##        bool: True if 'num' is prime. False otherwise.
##
##    Preconditions:
##        num > 1
##    """
##    i = 2
##    while i < num :
##        if num % i == 0 :
##            return False
##        i = i + 1
##    return True

def is_prime(num):
    """Returns True iff 'num' is prime.

    Parameters:
        num (int): Integer value to be tested to see if it is prime.

    Return:
        bool: True if 'num' is prime. False otherwise.

    Preconditions:
        num > 1
    """
    if num == 2 :
        return True
    elif num % 2 == 0 :
        return False
    
    sqrt_num = math.sqrt(num)
    i = 3
    while i <= sqrt_num :
        if num % i == 0 :
            return False
        i = i + 2
    return True


def next_prime(num) :
    """Returns the next prime number after 'num'.

    Parameters:
        num (int): Starting point for the search for the next prime number.

    Return:
        int: The next prime number that can be found after 'num'.

    Preconditions:
        num > 1
    """
    if num % 2 == 0 :
        next_number = num + 1
    else :
        next_number = num + 2
        
    # next_number is the next odd number after num
    while not is_prime(next_number) :
        next_number = next_number + 2
    return next_number


def nth_prime(n) :
    """Returns the n'th prime number.

    Parameters:
        n (int): The number of prime numbers to find.

    Return:
        int: The n'th prime.

    Preconditions:
        n > 0
    """
    next_prime_number = 2
    i = 1
    while i < n :
        # loop invariant: next_prime_number is the i'th prime
        i += 1
        next_prime_number = next_prime(next_prime_number)
    return next_prime_number


# example of use

print(nth_prime(7))
    
