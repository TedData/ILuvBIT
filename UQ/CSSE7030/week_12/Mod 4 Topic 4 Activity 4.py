import operator

list1 = [2,4,5,9]
list2 = [1,2,3,4]

print(list(map(operator.mod,list1,list2)))

