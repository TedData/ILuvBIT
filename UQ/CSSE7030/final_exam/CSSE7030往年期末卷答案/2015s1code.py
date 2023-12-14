#!/usr/bin/env python3

"""
2015s1code.py
This file contains code from CSSE1001 Semester 1 2015 Final Exam.
It also contains an interface to help in quickly executing code from questions.
"""

__author__ = 'Joshua Lee'
__date__ = '6 June 2018'
__copyright__ = 'Copyright 2015, UQ'

# SUPPORT

def g(x, z):
    x.append(z)
    return x

def md(x):
    a, b = x
    a, b = a // b, a % b
    return (a,b)

def fi(xs, n, m):
    s = xs[n]
    r = [s]
    while n < m:
        if xs[n] > s:
            s = xs[n]
            r.append(s)
        n += 1
    return r

def hti(xs, v, h):
    i = h
    inc = 0
    n = len(xs)
    while xs[i] is not None:
        if xs[i] == v:
            return
        inc += 1
        #print("i = ({0}+{1}) % {2}".format(i,inc%n,n))
        i = (i+inc) % n
    xs[i] = v

def create_data():
    """
    Creates data required for q24-26

    Return:
        (str): name of file created
    """
    name = 'values2015_1.txt'
    with open(name, 'w') as file_out:
        out = ''
        out += '1.2, 1 ,2.3, 1.4, 0.1\n'
        out += '0.7,1.5, 1.2, 2.4, 0.1\n'
        out += '2.1,0.7, 1.4, 2.0, 0.1'
        file_out.write(out)
    return name

def get_column_sums(filename):
    fd = open(filename, 'r')
    data = []
    for line in fd:
        parts = line.split(',')
        line_data = []
        for p in parts:
            line_data.append(float(p.strip())) ## line 1 ##
        data.append(line_data)
    column_sums = []
    for index in range(len(data[0])):
        colsum = 0
        for row in range(len(data)):
            colsum += data[row][index] ## line 2 ##
        column_sums.append(colsum) ## line 3 ##
    return column_sums

class Player(object):
    def __init__(self, name, health):
        self._name = name
        self._health = health
    def update_health(self, amount):
        """Update the players health by amount (may be negative)"""
        self._health += amount ## line 1 ##
    def get_health(self):
        """Return the players health."""
        return self._health ## line 2 ##

class A(object):
    def __init__(self, x):
        self.x = x
    def f(self, x):
        return self.g(x)+1
    def g(self, x):
        return x+1
    
class B(A):
    def g(self, y):
        return y + self.x

class C(B):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
        self.x += y
    def g(self, y):
        return y
    def f(self, x):
        return super().g(x) + self.y

class D(C):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.y = y + x
    def g(self, x):
        return x + self.x

a = A(2)
b = B(2)
c = C(2, 2)
d = D(2, 0)

import tkinter as tk

class ButtonsFrame(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent.root)
        b1 = tk.Button(self, text= "A")
        b2 = tk.Button(self, text = "B")
        b1.pack()
        b2.pack()

class MainWindow(object):
    def __init__(self, root):
        self.root = root
        label = tk.Label(root, text="Buttons")
        label.pack(side=tk.LEFT,expand=1)
        bf = ButtonsFrame(self)
        bf.pack(side=tk.LEFT, fill=tk.BOTH,expand=1)

class LinkedList:
    def __init__(self, head, tail):
        self._head = head
        self._tail = tail
    def head(self): return self._head
    def tail(self): return self._tail
    def isLast(self): return self._tail == None
    def values(self):
        result, scan = [], self
        while not scan.isLast():
            result.append(scan.head())
            scan = scan.tail()
        result.append(scan.head())
        return result

def concat(xs, ys):
    if xs.isLast():
        return LinkedList(xs.head(), ys)
    else:
        return LinkedList(xs.head(), concat(xs.tail(), ys))

def reverse(xs):
    result = []                 #1
    for x in xs:                #n
        result.insert(0, x)         #n
    return result               #1

#O(n^2)

def contains_increasing(xs, n):
    """Returns True iff xs contains an increasing sublist
    with at least n elements
    Precondition: len(xs) > 2 and n > 1
    """
    v = xs[0]                           #1
    c = 1                               #1
                                        #n for creating range, 1 for length calc
    for i in range(1, len(xs)):         #n
        if xs[i] > v:                       #1
            c += 1                              #1
            if c == n:                          #1
                return True
        else:                               #1
            c = 0                               #1
        v = xs[i]                           #1
    return False
#O(n)

def t(xs):
    return [[xs[i][j] for i in range(len(xs))] for j in range(len(xs[0]))]

# QUESTIONS

def q1():
    print('>>> 2.0 + 11/2')
    print(2.0 + 11/2)

def q2():
    print('>>> 2 * [’1’, ’3’]')
    print(2 * ['1', '3'])

def q3():
    print('>>> ’2’ + [’1’, ’3’]')
    print('2' + ['1', '3'])

def q4():
    print('>>> list(’2’) + [’1’, ’3’]')
    print(list('2') + ['1', '3'])

def q5():
    x = 'Very Naughty Boy'
    y = x[5]
    print(">>> x = 'Very Naughty Boy'")
    print('>>> y = x[5]')
    print('>>> y')
    print(y)

def q6():
    x = 'Very Naughty Boy'
    y = x[5:9]
    print(">>> x = 'Very Naughty Boy'")
    print('>>> y = x[5:9]')
    print('>>> y')
    print(y)

def q7():
    x = 'Very Naughty Boy'
    y = x[-7:-4]
    print(">>> x = 'Very Naughty Boy'")
    print('>>> y = x[-7:-4]')
    print('>>> y')
    print(y)

def q8():
    x = 'Very Naughty Boy'
    y = x[-3:-6:-1]
    print(">>> x = 'Very Naughty Boy'")
    print('>>> y = x[-3:-6:-1]')
    print('>>> y')
    print(y)

def q9():
    y = [1, 2, 3]
    g(y, 4).extend(g(y[:], 4))
    print(">>> y = [1, 2, 3]")
    print(">>> g(y, 4).extend(g(y[:], 4))")
    print(y)
    print(">>>")
    print(">>> #Note: y[:] is a copy of the list y. Thus, y[:] is passed by")
    print(">>> #value, while y is passed by reference.")

def q10():
    y = [1, 2, 3]
    g(y[:], 4).extend(g(y, 4))
    print(">>> y = [1, 2, 3]")
    print(">>> g(y[:], 4).extend(g(y, 4))")
    print(y)
    print(">>>")
    print(">>> #Note: y[:] is a copy of the list y. Thus, y[:] is passed by")
    print(">>> #value, while y is passed by reference.")

def q11():
    x = 'a,,b,c,d,\n'
    print(">>> x = 'a,,b,c,d,\n'")
    print(">>> x.strip().split(',')")
    print(x.strip().split(','))

def q12():
    d = {'Brisbane': {2013:24.1, 2014:24.2},
'Adelaide': {2012:22.1, 2013:22.6, 2014:22.8}}
    y = d.get('Brisbane', {}).get(2012)
    print(">>>    d = {'Brisbane': {2013:24.1, 2014:24.2}, \
'Adelaide': {2012:22.1, 2013:22.6, 2014:22.8}}")
    print('>>> y = d.get(’Brisbane’, {}).get(2012)')
    print('>>> y')
    print(y)

def q13():
    d = {'Brisbane': {2013:24.1, 2014:24.2},
'Adelaide': {2012:22.1, 2013:22.6, 2014:22.8}}
    y = d.get('Adelaide', {}).get(2012)
    print(">>>    d = {'Brisbane': {2013:24.1, 2014:24.2}, \
'Adelaide': {2012:22.1, 2013:22.6, 2014:22.8}}")
    print('>>> y = d.get(’Adelaide’, {}).get(2012)')
    print('>>> y')
    print(y)

def q14():
    n = md(md((20,3)))
    print('>>> n = md(md((20,3)))')
    print('>>> n')
    print(n)

def q15():
    n = md(md((30,2)))
    print('>>> n = md(md((30,2)))')
    print('>>> n')
    print(n)

def q16():
    n = md(md((3,20)))
    print('>>> n = md(md((3,20)))')
    print('>>> n')
    print(n)

def q17():
    x = fi([2,6,7,5,3,1], 2, 7)
    print('>>> x = fi([2,6,7,5,3,1], 2, 7)')
    print('>>> x')
    print(x)

def q18():
    x = fi([2,6,7,5,3,1], 2, -1)
    print('>>> x = fi([2,6,7,5,3,1], 2, -1)')
    print('>>> x')
    print(x)

def q19():
    x = fi([2,6,6,8,3,1], 0, 5)
    print('>>> x = fi([2,6,6,8,3,1], 0, 5)')
    print('>>> x')
    print(x)

def q20():
    x = fi([1, 4, 2, 4, 5], 1, 5)
    print('>>> x = fi([1, 4, 2, 4, 5], 1, 5)')
    print('>>> x')
    print(x)

def q21():
    xs = [None, 5, 6, None, 7]
    hti(xs, 8, 1)
    print(">>> xs = [None, 5, 6, None, 7]")
    print(">>> hti(xs, 8, 1)")
    print(xs)

def q22():
    xs = [2, 5, 9, 4, None, None, 7, None]
    hti(xs, 11, 0)
    print(">>> xs = [2, 5, 9, 4, None, None, 7, None]")
    print(">>> hti(xs, 11, 0)")
    print(xs)

def q23():
    xs = [2, 5, 9, 4, None, None, 7, None]
    hti(xs, 11, 3)
    print(">>> xs = [2, 5, 9, 4, None, None, 7, None]")
    print(">>> hti(xs, 11, 3)")
    print(xs)

def q24to26():
    print(">>> get_column_sums('values.txt')")
    print(get_column_sums(create_data()))

def q27to29():
    frodo = Player('Frodo', 10)
    frodo.update_health(-10)
    print(">>> frodo = Player('Frodo', 10)")
    print(">>> frodo.update_health(-10)")
    print(">>> frodo.get_health()")
    print(frodo.get_health())

def q30():
    print(">>> b.g(3)")
    print(b.g(3))

def q31():
    print(">>> a.f(3)")
    print(a.f(3))

def q32():
    print(">>> b.f(3)")
    print(b.f(3))

def q33():
    print(">>> c.f(3)")
    print(c.f(3))

def q34():
    print(">>> d.f(3)")
    print(d.f(3))

def q35and36():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

def q37():
    x = LinkedList(1,LinkedList(2, LinkedList(3,LinkedList(4,None))))
    y = LinkedList(5,LinkedList(6, LinkedList(7,LinkedList(8,None))))
    print(">>> x = LinkedList(1,LinkedList(2, LinkedList(3,LinkedList(4,None))))")
    print(">>> y = LinkedList(5,LinkedList(6, LinkedList(7,LinkedList(8,None))))")
    print(">>> x.values()")
    print(x.values())
    print(">>> y.values()")
    print(y.values())
    z = concat(x, y).values()
    print(">>> z = concat(x, y).values()")
    print(z)

def q38():
    print("Answer: Quadratic time. See code comments.")
    #function in question is annotated above

def q39():
    print("Answer: Linear time. See code comments.")
    #function in question is annotated above

def q40():
    y = t([[1,2,3],[4,5,6]])
    print(">>> y = t([[1,2,3],[4,5,6]])")
    print(y)

#UI

def main():
    print("CSSE1001 Semester 1 2015 Final Exam Code.\n")
    print("Enter a number from 1 to 40 to run commands/solutions for this exam.")
    print("If something doesn't work, it probably wasn't meant to.\n")
    debugging = True
    while debugging:
        print("\nOptions:")
        print("0. Exit")
        print("x. Run Qx solution (1 <= x <= 40)")
        selection = int(input("What do you want to do? "))
        
        print("")
        if selection == 0:
            debugging = False
        elif selection == 1:
            q1()
        elif selection == 2:
            q2()
        elif selection == 3:
            q3()
        elif selection == 4:
            q4()
        elif selection == 5:
            q5()
        elif selection == 6:
            q6()
        elif selection == 7:
            q7()
        elif selection == 8:
            q8()
        elif selection == 9:
            q9()
        elif selection == 10:
            q10()
        elif selection == 11:
            q11()
        elif selection == 12:
            q12()
        elif selection == 13:
            q13()
        elif selection == 14:
            q14()
        elif selection == 15:
            q15()
        elif selection == 16:
            q16()
        elif selection == 17:
            q17()
        elif selection == 18:
            q18()
        elif selection == 19:
            q19()
        elif selection == 20:
            q20()
        elif selection == 21:
            q21()
        elif selection == 22:
            q22()
        elif selection == 23:
            q23()
        elif selection in (24, 25, 26):
            q24to26()
        elif selection in (27, 28, 29):
            q27to29()
        elif selection == 30:
            q30()
        elif selection == 31:
            q31()
        elif selection == 32:
            q32()
        elif selection == 33:
            q33()
        elif selection == 34:
            q34()
        elif selection in (35, 36):
            q35and36()
        elif selection == 37:
            q37()
        elif selection == 38:
            q38()
        elif selection == 39:
            q39()
        elif selection == 40:
            q40()
        else:
            print("invalid selection")
            
    print("Goodbye.")
        

if __name__ == "__main__":
    main()
