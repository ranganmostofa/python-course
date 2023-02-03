file_name = input("Enter file name: ")

with open(file_name, "r") as file_obj:
    while line := file_obj.readline():
        # contents = file_obj.readline()
        # if len(contents) == 0:
        #     break
        print(line.upper(), end="")
