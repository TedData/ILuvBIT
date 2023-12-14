def add(num1,num2):
    """Function to return the result of adding num1 and num2

    Parameters
        num1(int): Integer value to be multiplied
        num2(int): Integer value to be multiplied

    Return:
        int: The sum, num1+num2
    """

    return num1+num2

def add2(num1,num2):
    print(num1+num2)

def mult(num1,num2):
    """Return the result of multiplying num1 and num2"""

    return num1*num2

def size(num):
    """Function to return 'One', 'Two' or 'Many' depending on num"""

    if num == 1:
        result = 'One'
    elif num == 2:
        result = 'Two'
    else:
        result = 'Many'
    return result

def sumto(n):
    """Return the sum of numbers from 1 to n (inclusive)"""

    total = 0
    m=1
    while n >= m:
        total=total+m  # can also use total+=m
        m=m+1
    return total

def sumto2(n):
    """Return the sum of numbers from 1 to n (inclusive)"""
    
    total = 0
    for m in range(1,n+1):
        total=total+m #total+=m
    return total


def factorial(n):
    """"Return n! (i.e. return n*(n-1)*n-2)....1"""

    total = 1
    for m in range(n,0,-1):
        total=total*m
        m=m+1
    return total


