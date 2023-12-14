class Person:
    def __init__(self):
        self.health = 100
        self.stamina = 100
    '''
    def getHit(self, amount):
        self.health -= amount

    def useSkill(self, x):
        self.stamina -= x'''

class Game:
    def __init__(self, person, name, age):
        self.person = person
        self.name = name
        self.age = age

    def printDetail(self):
        print("Name: " + self.name + "  Health: " + str(self.person.health) + "  Stamina: " + str(self.person.stamina))


player1 = Person()
TED = Game(player1, "Ted", "18")

TED.printDetail()

#TED.person.getHit(10)
TED.printDetail()
