
class Student(object):
    def __init__(self, name, snum):
        """Constructor: Student(str, str)"""
        self._name = name
        self._snum = snum
        self._courses = []
        self._results = {}
        
    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name=new_name

    def get_snum(self):
        return self._snum 
    
    def add_courses(self, courses):
        self._courses.extend(courses)

    def get_courses(self):
        return self._courses

    def add_results(self, results):
        self._results.update(results)

    def get_results(self):
        return self._results

    def __add__(self, f):
        return str(self._name) + ' and ' + str(f._name)
    
    def __str__(self):
        """ return the name of the student
        __str__() -> str
        """
        return "Student({0}, {1})".format(self._name, self._snum)

    def __repr__(self):
        return "Student({0}, {1})".format(self._name, self._snum)
    
class ExchangeStudent(Student):
    def __init__(self, name, snum, exchange_uni, date_of_exchange):
        super().__init__(name, snum)
        self._exchange_uni = exchange_uni
        self._date_of_exchange = date_of_exchange

    def get_exchange_uni(self):
        return self._exchange_uni

    def get_date_of_exchange(self):
        return self._date_of_exchange

    def __repr__(self):
        return "ExchangeStudent({0}, {1}, {2}, {3})".format(self._name, self._snum, self._exchange_uni, self._date_of_exchange)


