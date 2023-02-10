import math


s = set()
d = {}

print(type(s))
print(type(d))

#
# Both dicts and sets are concrete impl of abstract data structures
#
# Abstract -> Iterable
# Concrete -> List, Set, Tuple
#
# Abstract -> Hashset
# Concrete -> Set, Dictionary
#

s1 = {"first", "second", "third", "fourth"}
d1 = {
    "first": "a",
    "second": "b",
    "third": "c",

}
print(f"s1 is not ordered: {s1}")
print(d1["first"])
print(d1["second"])
# print(d1[4])
print(f"d1.get('first') is {d1.get('first')}")
print(d1.get(4, "defaultSKdgnskdgla"))
print(f"d1 is still: {d1}\n")

s2 = {d1.get(num) for num in s1}
print(f"s2 is not ordered: {s2}")

y_equals_x = {1: 1, 2: 2, 3: 3}
y_equal_x_squared = {x: x ** 2 for x in y_equals_x.keys()}
print(y_equal_x_squared)
print(list(y_equals_x.keys()))
print(y_equals_x.values())
y_equals_sq_root = {y: math.sqrt(y) for y in y_equal_x_squared.values()}
print(y_equals_sq_root)

print(d1)
print(d1.pop(3, "default"))
print(d1.pop(100, "default"))
print(d1)
print()

print(d1)
d1[3] = "c"
print(d1)

print(d1)
d1 = {**d1, 4: "d"}
print(d1)

print(d1)
d1.update(one="one", two=2, three=3)
print(d1)

print(d1)
d1 = {**d1, 4: "x"}
print(d1)

b = d1.items()
print(b)

print(d1.popitem())
