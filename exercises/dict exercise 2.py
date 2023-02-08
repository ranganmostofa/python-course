file_name = "mbox-short.txt"

dict1 = {}

with open(file_name, "r") as file_obj:
    while line := file_obj.readline():
        if "From " in line:
            if line.split()[1] not in dict1:
                dict1[line.split()[1]] = 1
            else:
                dict1[line.split()[1]] += 1

print(f"\ndict1 is {dict1}")

# Part 2

print(f"\nUsing max(dict1) outputs '{max(dict1)}' based on alphabet for keys")
print(f"Using max(dict1.keys()) outputs '{max(dict1.keys())}' same thing")
print(f"Using max(dict1.values()) simply outputs '{max(dict1.values())}' though there are duplicates")

max_num = None
max_key = None

for value in dict1.values():
    if max_num is None or value > max_num:
        max_num = value
        max_key = list(dict1.keys())[list(dict1.values()).index(value)]

print(f"\nFor the first for loop attempt:")
print(f"The max key is {max_key} and the max value is {max_num}")  # Not good code
print(dict1.values())
print(list(dict1.values())[0])

dict2 = {
    "A": 3,
    "B": 1,
    "C": 3,
    "D": 3,
    "E": 1,

}

max_num2 = None
max_key2 = None
list1 = []
for value2 in dict2.values():
    if max_num2 is None or value2 > max_num2:
        max_num2 = value2
        max_key2 = list(dict2.keys())[list(dict2.values()).index(value2)]
    elif max_num2 is None or value2 == max_num2:
        list1.append(list(dict2.keys())[list(dict2.values()).index(value2)])  # Doesn't work
        print(f"Duplicate(s) for max found: {list1}")

print(f"{max_key2}: {max_num2}")

print(f"max(dict2) outputs {max(dict2)}")
print(max(dict2.items()))
print(max(dict2.items(), key=lambda t: (t[1], t[0])))

dict3 = {}

for k, v in dict1.items():
    if v == max(dict1.values()):
        dict3[k] = v

print(f"Using max(dict1.values()) followed by a for loop to match keys to the max value gives {dict3}")
