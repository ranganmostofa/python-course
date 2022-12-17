num, check = int(input("Enter a number: ")), int(input("Enter a divisor: "))

if num % check == 0:
    print(f"{num} is a multiple of {check}.")
# elif num % 2 == 0:
#     print(f"{num} is even.")
else:
    print(f"{num} is not a multiple of {check}.")