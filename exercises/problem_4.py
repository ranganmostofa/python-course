import math


user_number = int(input("Give me a number: "))
# final_list = [num for num in x if user_number % num == 0]
first_half = [num for num in range(2, int(math.sqrt(user_number)) + 1) if user_number % num == 0]
second_half = [int(user_number/num) for num in reversed(first_half)]

# great code for someone like you, 
# for num in x:
#     if user_number % num == 0:
#         first_half.append(num)
#         second_half.append(int(user_number/num))
# final_list = first_half + list(reversed(second_half))
print(first_half + second_half)
