OPTIONS="""
Specify an action. The options are:

ac - add a course to an existing record
ar - add a result to an existing record
"""

class Student(object):
    def __init__(self, name, snum):
        """Constructor: Student(str, str)"""
        self._name = name
        self._snum = snum
        self._courses = []
        self._results = {}
        
    def get_name(self):
        return self._name

    def get_snum(self):
        return self._snum

    def get_courses(self):
        return self._courses
    
    def add_courses(self, courses):
        self._courses.extend(courses)

    def add_results(self, results):
        self._results.update(results)

    def get_results(self):
        return self._results
    
    
    def __repr__(self):
        return "Student({0}, {1})".format(self._name, self._snum)

    def __str__(self):
        return "Student({0}, {1})".format(self._name, self._snum)

#    def __lt__(self,f):
#        return self._snum < f._snum


class UpdateResults(object):
    def __init__(self):     
        print('Welcome to the University Student Record system\n')
        name=input('Input the name of the student of interest: ')
        snum=input('Input their student number: ')
        self._student_record=Student(name,snum)
        while True:
            subject=input('\nEnter subject: ')
            if subject=='':
                break
            grade=input('Enter grade: ')
            self._student_record.add_results({subject:grade})
        self.display_student_results()

    def display_student_results(self):
        print('\n Academic Record\n')
        print(self._student_record.get_name(),self._student_record.get_snum(),'\n')
        academic_record=self._student_record.get_results()
        for subject,grade in academic_record.items():
            print(subject, grade)        

app=UpdateResults()
    
