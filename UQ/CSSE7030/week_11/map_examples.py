import operator

def cube(x):
    return x**3

xs=[3,4,5,6]
g=map(cube, xs)
print(list(map(cube, xs)))

print(list(map(operator.mul, [1,2,3,4],2*[5,6,7,8])))

print(sum(list(map(operator.mul, [1,2,3,4],[5,6,7,8]))))
