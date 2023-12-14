def add_half(a,b):
	""" Add a to b/2
	"""
	return a+b/2

def second_function(function1):
	return function1(3,10)

def add_quarter(a,b):
	""" Add a to b/4
	"""
	return a+b/4

def third_function(function1,function2):
        return function1(3,10)+function2(3,10)

g=lambda x: 3+x



def square_elems(xs):
    """ Return the list of elements of xs
    square_elems(list(int)) => list(int)
    """
    r=[]
    for x in xs:
        r.append(x ** 2)
    return r

def square_elems2(xs):
    """ Return the list of elements of xs
    square_elems(list(int)) => list(int)
    """
    return [x**2 for x in xs]
        
def my_iter(xs):
    for x in xs:
        yield x

def my_iter2(xs):
    for x in xs:
        print('start',x)
        yield x
        print('finish',x)
   

def mycount(n):
    while True:
        yield n
        n+=1

def myzip(xs,ys):
    xs=iter(xs)
    ys=iter(ys)
    while True:
        try:
            x=next(xs)
            y=next(ys)
            yield (x,y)
        except:
            break
    
    
import random
def myshuffle(xs):
    """ Returns a shuffle of xs
    myshuffle(list(int))=> list(int)
    """
    ys=[(random.random(),x) for x in xs]
    ys.sort()
    return [x for y,x in ys]
    
    
        
