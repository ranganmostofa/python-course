class Calculator:

    def add(*args):
        return sum(args)

    def multiply(*args):
        x = 1
        for number in args:
            x *= number
            print(x)
        return x


example1 = Calculator()
print(example1.add(1, 2, 3, 4, 5))
print(example1.multiply(2, 3, 6, 8, 9))
