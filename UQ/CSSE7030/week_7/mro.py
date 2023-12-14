class A(object) :
    def __init__(self, x) :
        self._x = x

    def f(self) :
        return self._x

    def g(self) :
        return 2 * self._x

    def fg(self) :
        return self.f() - self.g()



class B(A) :
    def g(self) :
        return self._x ** 2



class C(B) :
    def __init__(self, x, y) :
        super().__init__(x)
        self._y = y

    def fg(self) :
        return super().fg() * self._y



class D(A) :
    def f(self) :
        return -2 * self.g()



# Example usage
a = A(3)
print(a.f(), a.g(), a.fg())

b = B(3)
print(b.f(), b.g(), b.fg())

c = C(3, 5)
print(c.f(), c.g(), c.fg())

d = D(3)
print(d.f(), d.g(), d.fg())

