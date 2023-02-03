file_name = "mbox-short.txt"

email_list = ""
with open(file_name, "r") as file_obj:
    while line := file_obj.readline():
        if "From " in line:
            print(line.split()[1])
