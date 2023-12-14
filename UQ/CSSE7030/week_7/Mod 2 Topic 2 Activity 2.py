
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

    #Activity 2
    def __add__(self, f):
        """ Add two student objects together """
        
        student = Student(self._name, self._snum)
        student.add_courses(self._courses)
        student.add_results(self._results)

        for course in f.get_courses():
            if course not in self._courses:
                student.add_courses([course])

        for key, value in f.get_results().items():
            if key not in self._results:
                student.add_results({key:value})
                
        return student
    
    def __str__(self):
        """ return the name of the student
        __str__() -> str
        """
        return "Student({0}, {1})".format(self._name, self._snum)

    def __repr__(self):
        return "Student({0}, {1})".format(self._name, self._snum)
