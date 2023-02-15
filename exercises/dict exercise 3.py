file_name = "mbox-short.txt"

dict1 = {}

with open(file_name, "r") as file_obj:
    while line := file_obj.readline():
        if "From " in line:
            email = line.split()[1]
            if email not in dict1:
                dict1[email] = 1
            else:
                dict1[email] += 1

print(f"\ndict1 is {dict1}")
print("testing")

dict2 = {}
for address, number in dict1.items():
    domain = address.split("@")[1]
    if domain not in dict2:
        dict2[domain] = number
    else:
        dict2[domain] += number
print(dict2)
print(list(dict1.items()))

list2 = [(c, e) for e, c in dict1.items()]

print(list2)

list2.sort(reverse=True)

print(list2)
