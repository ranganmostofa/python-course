import random


a = random.sample(range(101), 50)
b = random.sample(range(101), 50)

common = set(a).intersection(set(b))
# for item in a:
#     if item not in common and item in b:
#         common.append(item)

print(common)
