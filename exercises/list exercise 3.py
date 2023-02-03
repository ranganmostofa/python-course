
i = 0
listnum = []
while i != 5:
    num = int(input("Enter a number: "))
    listnum.append(num)
    i += 1
print(f"max number is: {max(listnum)}")
print(f"min number is: {min(listnum)}")
