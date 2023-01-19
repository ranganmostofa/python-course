# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# year_100 = 100 - age + 2022
# print(f"Your name is {name} and your age is {age}")
# print(f"You will be 100 on year: {year_100}")

# number1 = int(input("Enter your first number: "))
# number2 = int(input("Enter your second number: "))
#
# if number1 % number2 == 0:
#     print(f"{number1} is divisible by {number2} evenly.")
# else:
#     print(f"{number1} is NOT divisible by {number2} evenly.") # Does iff exist in python?
# if number1 % 2 == 0 and number1 % 4 != 0:
#     print(f"The number {number1} is even")
# elif number1 % 2 == 0 and number1 % 4 == 0:
#     print(f"The number {number1} is even and divisible by 4")
# else:
#     print(f"The number {number1} is odd")

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# c = int(input("Enter: "))
# # num2 = int(input("Enter a number: "))
# # for num1 in a:
# #     if num1 < num2:
# #         b.append(num1)
# # print(b)
# print([x for x in a if x < c])

# numb = int(input("Enter a number: "))
# divisors = [d for d in range(2, numb) if numb % d == 0]
# # for d in range(1, numb):
# #     if numb % d == 0:
# #         divisors.append(d)
# print(f"These are divisors of {numb}: {divisors}")

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # # # c = [numa for numa in a if numa in b and numa not in c]  # Can I reference a list within itself?
# c = list(set(a).intersection(set(b)))
# # c = []
# # for numa in a:
# #     if numa in b and numa not in c:
# #         c.append(numa)
# print(c)

# string1 = input("Enter a string: ")
# string_rev = string1[::-1]
# if string1 == string_rev:
#     print(f"{string1} is a palindrome")
# else:
#     print(f"{string1} is NOT a palindrome")

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = [num for num in a if num % 2 == 0 and num != 4]
# # b = [num if num % 2 == 0 or num not in b else "" for num in a]
# print(b)

# player1 = input("Enter player 1 choice: ")
# player2 = input("Enter player 2 choice: ")
# if player1 == player2:
#     print("It's a tie.")
# elif player1 == "rock":
#     if player2 == "scissors":
#         print("Player 1 wins with rock")
#     else:
#         print("Player 2 wins with paper")
# elif player1 == "paper":
#     if player2 == "rock":
#         print("Player 1 wins with paper")
#     else:
#         print("Player 2 wins with scissors")
# elif player1 == "scissors":
#     if player2 == "paper":
#         print("Player 1 wins with scissors")
#     else:
#         print("Player 2 wins with rock")

import random
a = random.randint(1, 9)
print(f"The answer is {a}")

for c in range(1, 3):
    guess_str = input("Guess what number 1-9 I'm thinking: ")
    if guess_str.lower() == "exit":
        break
    guess_num = int(guess_str)
    if guess_num < a:
        print("Too low, try again")
    elif guess_num > a:
        print("Too high, try again")
    elif guess_num == a:
        print(f"You got it!")
        break
print("Game Over".center(40, "~"))
print(f"The number was {a}" 
      f"\nNumber of guesses: {c}")

# print(random.sample(range(1, 30), 5))  # Random list generator

# number = int(input("Enter a positive number to see if it's prime: "))  # How to also show divisors if not prime?
# d = [x for x in range(2, number - 1) if number % x == 0]
#
# if d:
#     d.extend([1, number])
#     d.sort()
#     print(f"The number {number} is not prime")
#     print(f"Divisors: {d}")                     # Can I call a function when printing inside {} ?
# else:
#     d.extend([1, number])
#     print(f"The number {number} is prime")
#     print(f"Divisors: {d}")

# a = [5, 10, 15, 20, 25]
# def listfunction(list1):
#     print([list1[0], list1[-1]])
# listfunction(a)
# # b = [a[0], a[-1]]
# # print(b)
#
# input_a = int(input("Enter how many fib you want: "))


# def fib_gen(x):
#     # fib_list = [0, 1]
#     # while len(fib_list) - 1 < x:
#     #     fib_list.append(fib_list[-1] + fib_list[-2])
#     fib_list = []                                       # Can't have while loops in list comprehensions?
#     fib_cur = 0
#     fib_last = 1
#     # # # fib_next = 1
#     # # # while len(fib_list) != x:
#     # # #     fib_last = fib_cur
#     # # #     fib_cur += fib_next
#     # # #     fib_next = fib_last
#     # # #     fib_list.append(fib_cur)
#     while len(fib_list) != x:
#         fib_list.append(fib_cur + fib_last)
#         fib_last = fib_cur
#         fib_cur = fib_list[-1]
#     # fib_list.remove(0)
#     print(fib_list)
#
#
# fib_gen(input_a)


# def simplify(list1):
#     # list2 = []
#     # for x in list1:
#     #     if x not in list2:
#     #         list2.append(x)
#     list2 = list(set(list1))
#     print(list2)
#
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# simplify(a)

# def word_rev(string1):
#     string2 = " ".join(string1.split()[::-1])
#     print(string2)
#
#
# string3 = "this is a string"
# word_rev(string3)
