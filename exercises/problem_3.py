a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user_number = input("Give me a number bitch: ")
print(list(valid for valid in a if valid < int(user_number)))