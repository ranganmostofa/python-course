file_name = "mbox-short.txt"

with open(file_name, "r") as file_obj:
    while line := file_obj.readline():
        if line.startswith("From "):
            print(line.split()[1])
