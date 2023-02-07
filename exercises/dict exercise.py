dict1 = {
    'Mon': 0,
    'Tue': 0,
    'Wed': 0,
    'Thu': 0,
    'Fri': 0,
    'Sat': 0,
    'Sun': 0,

}

print(dict1["Mon"])

file_name = "mbox-short.txt"

with open(file_name, "r") as file_obj:
    while line := file_obj.readline():
        if "From " in line:
            dict1[line.split()[2]] += 1

print(dict1)
print(dict1.items())

for key, value in dict1.items():
    if dict1[key] != 0:
        print(key, value)

for key in dict1:
    if dict1[key] != 0:
        print(key, dict1[key])

dict2 = {}

for key, value in dict1.items():
    if dict1[key] != 0:
        dict2[key] = value

print(dict2)

for key2, value2 in dict2.items():
    print(key2, value2)
