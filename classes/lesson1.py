class Mammal:
    def __init__(self, name, age, gender, hair_color=None, children=None, *args, **kwargs):
        self.name = name
        self.age = age
        self.gender = gender
        self.hair_color = hair_color

        self.children = children or []
        self.number_of_children = len(self.children)

        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return self.name

    def __add__(self, other):
        return self.name, other.name

    def eat(self):
        pass

    def sleep(self):
        pass

    def do_life(self):
        self.eat()
        self.sleep()


class Dog(Mammal):
    def __init__(self, name, age, gender, paw_count=4, hair_color=None, children=None):
        super().__init__(name=name, age=age, gender=gender, hair_color=hair_color, children=children)
        self.paw_count = paw_count

    def eat(self):
        print(f"{self} ate dog food")


class Person(Mammal):
    def __init__(self, name, age, gender, leg_count=2, hair_color=None, children=None, office=None):
        super().__init__(name=name, age=age, gender=gender, hair_color=hair_color, children=children)
        self.leg_count = leg_count
        self.office = office or "unemployed"

    def do_life(self):
        self.work()
        super().do_life()

    def work(self):
        print(f"{self} worked at {self.office} office")

    def eat(self):
        print(f"{self} ate meat")


# jason = Person(24, "female", "blonde", [])
jason = Person("Jason", 24, "female", hair_color="black", office="Grid United")
print(jason.number_of_children)
carlos = Person("Carlos", 24, "male", hair_color="black")

jason.children.append("harris")
print(jason.children)
print(carlos.children)

ragib = Person("Ragib", 26, "male", children=[], hair_color="black")
print(ragib.age)
print(ragib.gender)
print(ragib.hair_color)
print(ragib.children)
print(ragib.args)
print(ragib.kwargs)

jason.do_life()
# carlos.do_life()

dog = Dog("Kodiak", 2, "male")
dog.do_life()

print(dog)

print(dog + jason)
