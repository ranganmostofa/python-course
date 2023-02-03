temp_celsius = int(input("Enter a Celsius temperature: "))


def convert_temp(temperature):
    temp_fahrenheit = temperature * 1.8 + 32
    print(f"{temp_celsius} degrees Celsius is equal to {temp_fahrenheit} degrees Fahrenheit")


convert_temp(temp_celsius)
