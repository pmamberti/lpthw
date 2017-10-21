## Animal is-a object (yes sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal and has-a def__init__
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

##??
class Person(object):

    def __init__(self, name):
        ##??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

##??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## MAry has-a pet: satan
mary.pet = satan

## Frank is-a Employee and has-a salary of 120000
frank = Employee("Frank"", 120000)

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
