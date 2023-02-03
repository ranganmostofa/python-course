i = 0
listnum = []
num = ""
while num != "done":
    num = input("Enter a number: ")
    if num == "done":
        break
    listnum.append(int(num))
print(f"max number is: {max(listnum)}")
print(f"min number is: {min(listnum)}")
