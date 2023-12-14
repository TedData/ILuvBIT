#from student_solution import *

#class StudentInformation
#student_information

#class Student(object):
#class Student():
class Student:

    def some_other_method(self, name, snum, address):
        print(name, snum, address)

        
    def __init__(self, name, snum, address):
        """Constructor: Student(str, str)"""
        self._name = name
        self._student_num = snum
        self._address = address
        self._courses = []
        self._results = {}

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name=new_name

    def get_snum(self):
        return self._student_num

    def add_courses(self, courses):
        self._courses.append(courses)

    def get_courses(self):
        return self._courses

    def add_results(self, results):
        self._results.update(results)

    def get_results(self):
        return self._results

    def __str__(self):
        """ return the name of the student
        __str__() -> str
        """
        return 'string'
        #return "Student({0}, {1})".format(self._name, self._student_num)

    def __repr__(self):
        return 'repr'
        #return "Student({0}, {1}, {2})".format(self._name, self._student_num, self._address)
    

#student = Student("Johnny Bravo", "abc", True)

