import itertools

def isnotdiv(p) :
    return lambda v: (v % p) != 0

def primes() :
    ints = itertools.count(2)
    while True :
        prime = next(ints)
        yield prime
        ints = filter(isnotdiv(prime), ints)
