filename = input("Enter a filename: ")


line_count = 0
with open(filename, "r") as file_obj:
    while line := file_obj.readline():
        if line.startswith("From "):
            line_count += 1
            _, email, *remaining = line.split()
            print(email)

print(line_count)
