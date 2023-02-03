file_name = "romeo.txt"

wordlist = set()
with open(file_name, "r") as file_obj:
    while line := file_obj.readline():
        wordlist |= set(line.split())
print(sorted(list(wordlist)))
