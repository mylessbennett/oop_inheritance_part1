class Person:
    """ Creates a person """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        return "Hello my name is {}".format(self.name)


class Student(Person):
    """ Made to learn """

    def learn(self):
        return "I get it!"


class Instructor(Person):
    """ Made to teach """

    def teach(self):
        return "An object is an instance of a class."


nadia = Instructor('Nadia')
chris = Student('Chris')

print(nadia.greeting())
print(chris.greeting())

print(nadia.teach())
print(chris.learn())
# chris.teach()<-- getting error message saying Student doesn't have teach
# attrib because it is inheriting from Person which doesn't have teach method
