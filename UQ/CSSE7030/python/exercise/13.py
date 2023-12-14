#用匿名函数给dict排序
students=[{'name':'Ted','age':30},{'name':'Kelvin','age':27}]
students.sort(key=lambda x: x['age'])
print(students)