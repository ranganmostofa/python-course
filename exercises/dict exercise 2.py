file_name = "mbox-short.txt"

dict1 = {}

with open(file_name, "r") as file_obj:
    while line := file_obj.readline():
        if "From " in line:
            if line.split()[1] not in dict1:
                dict1[line.split()[1]] = 1
            else:
                dict1[line.split()[1]] += 1

print(dict1)
