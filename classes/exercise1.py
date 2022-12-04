class Calculator:

    def __init__(self):
        pass

    @staticmethod
    def add(*args):
        """
        Comment here
        """
        return sum(args)

    @staticmethod
    def multiply(*args):
        x = 1
        for number in args:
            x *= number
            print(x)
        return x


# example1 = Calculator()
print(Calculator.add(1, 2, 3, 4, 5))
print(Calculator.multiply(2, 3, 6, 8, 9))
