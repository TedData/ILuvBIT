# The original functions

def my_sum(lst) :
    result = 0
    for x in lst :
        result += x
    return result

def product(lst):
    result = 1
    for x in lst :
        result *= x
    return result


# Redefined using the combine function.

def combine(operation, lst, initial):
    result = initial
    for x in lst :
        result = operation(result, x)
    return result

def my_sum2(lst) :
    return combine(lambda x,y: x+y, lst, 0)

def product2(lst) :
    return combine(lambda x,y: x*y, lst, 1)

def concat(strings) :
    return combine(lambda x,y: x+y, strings, '')


# Example use
if __name__ == "__main__" :
    print(my_sum2([1,2,3,4]))
    print(product2([1,2,3,4]))
    print(concat(['a','b','c']))
