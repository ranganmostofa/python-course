from datetime import datetime


name = input("Enter name: ")
age = int(input("Enter age: "))
now = datetime.now().year

print(f"{name}, you will turn 100 years old in {now + (100 - age)}")
