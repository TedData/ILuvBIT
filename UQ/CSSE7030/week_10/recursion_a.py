def sumto(n):
    """ Return the sum of numbers from 0 to n

    sumto(int) -> int

    Precondition: n >= 0
    """

    if n == 1:
        # base case
        return 1
    else:
        return n + sumto(n-1)

def sumto_2(n):
    """ Return the sum of numbers from 0 to n

    sumto(int) -> int

    Precondition: n >= 0
    """

    if n == 1:
        # base case
        print("n = ", n, ";  n+(n-1) = ",n+(n-1) )
        return 1
    else:
        print("n = ", n)
        m = sumto_2(n-1)
        print("n = ", n, ";  n+sumto(n-1) = ", m+n)
        return m + n



def is_palindrome(s):
    """Return True iff s is a palindrome

    is_palindrome(str) -> boolean
    """
    if len(s) < 2:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])
        
def is_palindrome_2(s):
    """Return True iff s is a palindrome

    is_palindrome(str) -> boolean
    """
    if len(s) < 2:
        print(s, True) 
        return True
    else:
        m=s[0] == s[-1] and is_palindrome_2(s[1:-1])
        print(s, m)
        return m
    
def max_of_list(xs):
    """Return the max elem of a non-empty list


    max_of_list(list(X)) -> X
    """
    if len(xs) == 1:
        return xs[0]
    else:
        m = max_of_list(xs[1:])
        if m < xs[0]:
            return xs[0]
        else:
            return m

def max_list(xs):
    if len(xs) == 1:
        return xs[0]
    else:
        return max(xs[0],max_list(xs[1:]))
    
