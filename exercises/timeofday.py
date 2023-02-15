file_name = "mbox-short.txt"

dict1 = {}

with open(file_name, "r") as file_obj:
    while line := file_obj.readline():
        if "From " in line:
            print(line)
            hour = line.split()[5].split(":")[0]
            if hour not in dict1:
                dict1[hour] = 1
            else:
                dict1[hour] += 1

print(f"\ndict1 is {dict1}")

for h, c in sorted(list(dict1.items())):
    print(f"{h} {c}")

