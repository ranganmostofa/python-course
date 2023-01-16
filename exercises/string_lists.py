word = input("Enter a word: ")

is_pal = True
start, end = 0, len(word) - 1
while start < end:
    if word[start] != word[end]:
        is_pal = False
    start, end = start + 1, end - 1

print(f"{word} is{' not' if not is_pal else ''} a palindrome")
