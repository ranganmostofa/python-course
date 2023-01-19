list1 = [1, 2, 3, 4, 5, 2]
set1 = set(list1)
print(set1)


class Number:
    def __init__(self, num):
        self.value = num


class Document:
    def __init__(self, idno):
        self.idno = idno
        # self.text = load_from_backend_db(idno)

empty_set = set()
print(empty_set)

list2 = [Number(1), Number(2), Number(2)]
print(list2)
print(f"[{', '.join(str(num.value) for num in list2)}]")
set2 = set(list2)
print(set2)

# functions of sets

set3 = {1, 2, 3, 4, 5}
set4 = {3, 4, 5, 6, 7}

set3.remove(1)
print(set3)

set3.pop()
print(set3)

set5 = set3.copy()
print(set5)

set3.clear()
print(set3)

print(set5)
set5.add(2)
print(set5)
set5.add(3)
print(set5)

set6 = set5.difference({4, 5})
print(set6)

set5.difference_update({4, 5})
print(set5)

set5.discard(2)
print(set5)

set5.discard(5)
# set5.remove(5)
print(set5)

print()
print(set4)
print(set5)
set10 = set5.intersection(set4)
print(set10)

print()
print(set4)
print(set5)
set10 = set5.union(set4)
print(set10)

print(set5.issubset(set4))
print(set5.issubset(set5))
print()
print(set4.issuperset(set5))
print(set4.issuperset(set4))
print()

set11 = {1, 2}
set12 = {3, 4}
print(set11.isdisjoint(set12))
print()

print(set5)
print(set4)
print(set5.symmetric_difference(set4))
print()

# symbolic ops
print(set4 - set5)
print(set4 & set5)
print(set4 | set5)
print()

set1.update(set2, set3, set4, set5)
print(set1)
print()

print(1 in set1)
print(1 in list(set1))
print()


# show deduplication algo
print("show deduplication algo")


from typing import List


def deduplicate(nums: List[Number]) -> List[Number]:
    seen = set()
    deduplicated_nums = []
    for number in nums:
        if number.value not in seen:
            deduplicated_nums.append(number)
            seen.add(number.value)
    return deduplicated_nums


def display_nums_list(nums: List[Number]) -> None:
    print(f"[{', '.join(str(num.value) for num in nums)}]")


list3 = [Number(1), Number(2), Number(2)]
display_nums_list(list2)
list4 = deduplicate(list3)
display_nums_list(list4)
