l = [1, 2, 3, 4]


def iterator_of_l():
    for item in l:
        yield item
        print("end of iteration")


iterator = iterator_of_l()

print(l)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
