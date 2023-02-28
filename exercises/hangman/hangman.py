word = input("Host select a word: ")
error_counter = 0
max_errors = 5
letter_list = set()
word_play = ["_"] * len(word)
guess = "a"

print(word_play)
while error_counter != max_errors:
    if "_" in word_play:
        guess = input("Select a letter: ").lower()
        if not guess.isalpha():
            print("Please enter a letter")
            continue
        if len(guess) > 1:
            print("Please enter only one letter")
            continue
        if guess not in letter_list:
            letter_list.add(guess)
            if guess in word:
                counter = -1
                for letter in word:
                    counter += 1
                    if guess == letter:
                        word_play[counter] = letter
                print("You got one!")
                print(f"You have {max_errors - error_counter} mistakes left")
                print(word_play)
            else:
                error_counter += 1
                print(f"You have {max_errors - error_counter} mistakes left")
                print(word_play)
        else:
            print("You already guessed that letter")
    else:
        print("You won!")
        break
else:
    print("Game Over: too many mistakes")
