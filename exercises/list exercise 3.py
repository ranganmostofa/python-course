listnum = []
while True:
    try:
        num = input("Type a number: ")
        if num == "done":
            break
        listnum.append(int(num))
    except ValueError:
        print("This is not a whole number.")
    # num = input("Enter a number: ")
print(f"max number is: {max(listnum)}")
print(f"min number is: {min(listnum)}")
