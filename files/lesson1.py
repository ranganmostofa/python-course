# file_obj = open("./data.csv", "r")
# header = file_obj.readline()
# print(header)
# contents = file_obj.read()
# print(contents)
# file_obj.close()

with open("./data.csv", "r") as file_obj:
    header = file_obj.readline()
    print(header)
    contents = file_obj.read()
    print(contents)


class A:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with A() as a:
    pass
