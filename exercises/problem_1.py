from datetime import date


name, age = input("What is your name: "), input("What is your age: ")
curr_yr = date.today().year
centennial_yr = curr_yr + (100-int(age))
multiplier = input("Give me a number: ")

for _ in range(int(multiplier)):
    print(f"{name}, you will turn into an old fart in {centennial_yr}")

