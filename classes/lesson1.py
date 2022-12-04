class Person:
    def __init__(self, age, gender, hair_color=None, children=None, *args, **kwargs):
        self.age = age
        self.gender = gender
        self.hair_color = hair_color

        self.children = children or []
        self.number_of_children = len(self.children)

        self.args = args
        self.kwargs = kwargs

    def do_life(self):
        self.work()
        self.eat()
        self.sleep()

    def work(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# jason = Person(24, "female", "blonde", [])
jason = Person(24, "female", "black")
print(jason.number_of_children)
carlos = Person(24, "male", "black")

# jason.do_life()
# carlos.do_life()

jason.children.append("harris")
print(jason.children)
print(carlos.children)

ragib = Person("male", 26, [], "black", 1, 2, 3, a=1, b=2, c=3)
print(ragib.age)
print(ragib.gender)
print(ragib.hair_color)
print(ragib.children)
print(ragib.args)
print(ragib.kwargs)
