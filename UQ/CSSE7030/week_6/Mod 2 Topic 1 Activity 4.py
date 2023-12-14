
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

    #ACTIVITY 4 method
    def change_of_grade(self, change_dict):
        """ Changes the grade of a subject.

        Parameters:
            Dictionary of the changes in the format:
            sample_change_dict={‘CSSE1001’:[3, 4], ‘ECON1010’:[5,6]}
            The first number in the list is the old grade and the second number is the new grade.
        """
        
        for key, value in change_dict.items():

            #error checking
            if key not in self._results:
                print("Error: Cannot change grade for {} as it has not been graded".format(key))
                return
            if self._results[key] != value[0]:
                print("Error: The old grade for {} was entered as {}, however it was actually {}".format(key, value[0], self._results[key]))
                return
            
            self._results[key] = value[1]

    def __add__(self, f):
        return str(self._name) + ' and ' + str(f._name)
    
    def __str__(self):
        """ return the name of the student
        __str__() -> str
        """
        return "Student({0}, {1})".format(self._name, self._snum)

    def __repr__(self):
        return "Student({0}, {1})".format(self._name, self._snum)
    
