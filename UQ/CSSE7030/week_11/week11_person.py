class Person:
    """Simple class for modelling a person with children"""
    def __init__(self, name):
        """Constructor

        Parameters:
            name(str): name of the Person
        """
        self._name = name
        self._children = []

    def get_children(self):
        """returns list<Person>"""
        return self._children

    def add_child(self, child):
        """
        adds the person as a child provided
        they are not already a child, and child
        is not self's parent

        Parameters:
            child(Person): child to add
        """
        if child not in self._children and \
           self not in child.get_children():
            self._children.append(child)

    def num_descendants(self):
        # replace this section with your code
        pass

    def has_descendant(self, person):
        # replace this section with your code
        pass

    def __repr__(self):
        return f'Person({self._name})'


# Use this family to test your code - add more members as required!

#          Bob          Fred
#           |
#         Bob Jr.
#           |
#         Bobby
#         /   \
# Mortimer    Lil' Bobby Tables

bob = Person('Bob')
fred = Person('Fred')

bob_jr = Person('Bob Jr.')
bob.add_child(bob_jr)

bobby = Person('Bobby')
bob_jr.add_child(bobby)

lil_bobby_tables = Person("Lil' Bobby Tables")
bobby.add_child(lil_bobby_tables)

mortimer = Person('Mortimer')
bobby.add_child(mortimer)