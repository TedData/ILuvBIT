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
    
                 
    
### Towers of Hanoi


def towers(from_pole, to_pole, other_pole, n):
    """ Print out instructions for moving a tower of
    n disks from the from_ slot to the to slot.
    d is not really required
    """
    if n == 0:
        return
    else:
        towers(from_pole, other_pole, to_pole, n-1)
        print("Move disc from {0} to {1}".format(from_pole, to_pole))
        towers(other_pole, to_pole, from_pole, n-1)

#towers('A', 'B', 'C', 4)


### Kosh snowflake


import turtle
# turtle.reset()  - reset the turtle
# turtle.up() down() - lift/drop pen
# turtle.left(angle) right(angle) - turn
# turtle.forward(dist) - move forward
# turtle.color(colour) - change colour
# turtle.begin_fill() turtle.end_fill()- start/stop filling
# turtle.speed(speed) - set speed - 'fast' 'fastest'

def eg():
    turtle.reset()
    turtle.up()
    turtle.goto(-200,-150)
    turtle.down()
    turtle.speed('fastest')
    turtle.begin_fill()
    turtle.color('blue')
    turtle.forward(400)
    turtle.left(120)
    turtle.forward(400)
    turtle.left(120)
    turtle.forward(400)
    turtle.left(120)
    turtle.end_fill()

#eg()

def koch(depth, size):
    """Draw a koch snowflake to given depth and size"""
    turtle.reset()
    turtle.up()
    turtle.goto(-200,-150)
    turtle.down()
    koch_edge(depth, size)
    turtle.left(120)
    koch_edge(depth, size)
    turtle.left(120)
    koch_edge(depth, size)
    

    
def koch_edge(depth, size):
    """Draw an edge to given depth and size finishing in the same direction
    that we started in"""
    if depth == 0:
        turtle.forward(int(size))
    else:
        koch_edge(depth-1, size/3)
        turtle.right(60)
        koch_edge(depth-1, size/3)
        turtle.left(120)
        koch_edge(depth-1, size/3)
        turtle.right(60)
        koch_edge(depth-1, size/3)
       
#koch(3, 200) 



