import math


user_input = input("Type one word only please: ")

midpoint = int(math.floor(len(user_input) / 2))
is_pal = all(
    character == user_input[len(user_input) - 1 - index]
    for index, character in enumerate(user_input[:midpoint])
)

# for index, character in enumerate(user_input[:endpoint]):
#     if character != user_input[len(user_input) - 1 - index]:
#         is_pal = False
#         break

print(f"{user_input} is{' not' if not is_pal else ''} a palindrome")
print(is_pal)
# if is_pal:
#     print(f"{user_input} is a palindrome")
# else:
#     print(f"{user_input} is not a palindrome")