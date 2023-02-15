from collections import defaultdict

file_name = "letter-frequency.txt"

dict1 = defaultdict(lambda: 0)

with open(file_name, "r") as file_obj:
    while line := file_obj.readline():
        line.lower()
        for letter in line:
            if 97 <= ord(letter) <= 122:
                dict1[letter] += 1
list1 = sorted(sorted(dict1.items()), key=lambda t: t[1], reverse=True)

print(dict1)
print(dict1.items())

for l, c in list1:
    print(f"{l}: {c}")
