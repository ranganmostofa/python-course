class Calculator:
    """
    Implement a calculator that does addition and multiplication
    """
    def __init__(self):
        pass

    def multiply(self, *args):
        product = 1
        for num in args:
            product *= num
            print(product)
        return product


    def add(self, *args):
        return sum(args)

easycalc = Calculator()
# print(easycalc.multiply(3,4))
# print(easycalc.add(5,10,15,30))
# print(easycalc.multiply(1,2,3,43))
