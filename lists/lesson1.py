# l1 = []
# l2 = [1, 2, 3]
# l3 = [1, "a", 3]
#
# print(len(l1))
# print(len(l2))
# print(len(l3))

# print(l1)
# l1.append(5)
# print(l1)
# print(len(l1))
#
# print(l2)
# l2.append(5)
# print(l2)
# print(len(l2))
#
# l2.extend(l3)
# print(l2)

# l4 = []
# for item in l2:
#     l4.append(item)
# for item in l3:
#     l4.append(item)
# print(l4)
#
# l5 = l2 + l3
# print(l5)
#
# l6 = [*l2, *l3]
# print(l6)
#
# print(l2)
# print(*l2)
#
# d1 = {"a": 1, "b": 2}
# kwargs = {"learning_rte": 0.01}
# # print(**d1)
#
#
# def train(blah, blah2, learning_rate):
#     print(learning_rate)
#
#
# train(1, 2, **kwargs)


# rand_list = [5, 12, 6, 7, 8, 1232, 3224]
# rand_list.sort()
# print(rand_list)
#
# rand_list2 = ["a", "}", ":"]
# rand_list2.sort()
# print(rand_list2)
# rand_list2.sort(reverse=True)
# print(rand_list2)
#
# rand_list3 = ["aaaa", "}}", ":"]
# rand_list3.sort(key=len, reverse=True)
# print(rand_list3)


# def fn(string):
#     # return sum(map(ord, string))
#
#     return sum(ord(char) for char in string if len(char) == 1)
#
#     # ascii = 0
#     # for char in string:
#     #     ascii += ord(char)
#     # return ascii
#
#
# rand_list3 = ["aaaa", "}", "::::::"]
# # rand_list3.sort(key=fn, reverse=True)
# # print(rand_list3)
# #
#
# rand_list4 = sorted(rand_list3)
# print(rand_list3)
# print(rand_list4)
#
# list1 = [1, 2, 3, 4]
# list1.reverse()
# print(list1)

# list2 = reversed(list1)
# print(list1)
# print(list(list2))

# list3 = list1.copy()
# print(list1)
# print(list3)
#
# list3.clear()
# print(list1)
# print(list3)


# list1 = [1, 2, 3, 4]
# lol = [1, 2, [3, 4]]
# list5 = lol.copy()
# print(lol)
# print(list5)
#
# lol[2][0] = "wtf"
# lol[0] = "wtf2"
# print(lol)
# print(list5)

# from copy import deepcopy
#
# list6 = deepcopy(lol)
# print(lol)
# print(list6)
#
# lol[2][0] = "wtf"
# lol[0] = "wtf2"
# print(lol)
# print(list6)
#
# list7 = [3, 4, 5, [0, 9]]
# list8 = list(list7)
# list8[-1][0] = "wtf"
# print(list7)
# print(list8)

list7 = [5, 4, 5, 5]
print(list7.count(5))
print(list7.index(5))
indices_of_5 = (
    index
    for index, item in enumerate(list7)
    if item == 5
)
# for index, item in enumerate(list7):
#     if item == 5:
#         indices_of_5.append(index)
print(indices_of_5)

list7.insert(0, "this is where")
print(list7)

# string = list7.pop(0)
# print(string)
# print(list7)

list7.remove("this is where")
print(list7)

# list7.remove("this is")
# print(list7)

del list7[1]
print(list7)
