a = str("ragib")
# a[2] = "k"

# # garbage collector
# a = "not ragib"

b = a[:2] + "K" + a[3:]
print(b)

string = "this IS a string. This is another sentence...."
print(len(string))

print(", ".join(["ragib", "jason", "carlos"]) + " are dumb.")

start = 0
target_indices = []
try:
    while True:
        next_i = string.index("i", start)
        target_indices.append(next_i)
        start = next_i + 1
except ValueError:
    pass

print(target_indices)

print(string.capitalize())
print(string.lower())
print(string.upper())
print(string[1].isupper())
print(string[1].islower())
print(string[1].upper().isupper())
print(string[1].upper().islower())
print(string)

print(string.center(100, "#"))

print(string.endswith("..."))
print(string.startswith("this"))

print()
print("2".isdigit())
print("2".isdecimal())
print("2".isnumeric())
print("2.0".isdigit())
print("2.0".isdecimal())
print("2.0".isnumeric())

try:
    _ = float("2.23123a113122")
    print(True)
except ValueError:
    print(False)

print()
print("try".isidentifier())
print("afal;dj".isidentifier())

name = "Carlos"
print()
print(f"My name is {name}")
print("My name is {name} {last_name}.".format(name=name, last_name="Fabian"))
print("The area of your rectangle is {}cm\u00b3".format("213213"))

str2 = ".......Hey .... there......."
print(str2.strip("."))
print(str2.lstrip("."))
print(str2.rstrip("."))

str3 = "carlos, jason, rangan, pratik, deepu, abdi"
print(str3.split(", "))
print(str3.rsplit(", ", maxsplit=3))

bicc_boi = """This is the first line.
This is the second line.
This is the final line."""
print(bicc_boi.split("\n"))
print(bicc_boi.splitlines())

str3 = ".......Hey .... there......."
print(str3.removeprefix("..."))
print(str3.removesuffix("..."))
