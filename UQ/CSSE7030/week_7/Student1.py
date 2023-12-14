
class Student(object):
    def __init__(self, name, snum, address):
        """Constructor: Student(str, str)"""
        self._name = name
        self._snum = snum
        self._address = address
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
        return "Student({0}, {1}, {2})".format(self._name, self._snum, self._address)
    
class TransferStudent(Student):
    def __init__(self, name, snum, address, transfer_uni):
        super().__init__(name, snum, address)
        self._transfer_uni=transfer_uni
        self._credit_courses=[]

    def assign_credit(self, courses):
        self._credit_courses.extend(courses)

    def get_credit(self):
        return self._credit_courses

    def __repr__(self):
        return "TransferStudent({0}, {1}, {2}, {3})".format(self._name, self._snum, self._address, self._transfer_uni)
    
    
