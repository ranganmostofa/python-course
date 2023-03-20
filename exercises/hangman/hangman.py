from english_words import get_english_words_set

from hangman_constants import GuessValidationCode, GUESS_VALIDATION_CODE_MAP
from hangman_utils import choose_word, show_progress, validate_guess


word_set = get_english_words_set(['web2'], alpha=True, lower=False)
word = choose_word(word_set)
error_counter = 0
max_errors = 5
used_letters = set()
word_play = ["_"] * len(word)

print(word)  # Test to see what the word is

while error_counter != max_errors:
    show_progress(word_play)
    if "_" in word_play:
        guess = input("Select a letter: ").lower()

        code = validate_guess(guess, used_letters)
        msg = GUESS_VALIDATION_CODE_MAP[code]
        if code != GuessValidationCode.SUCCESS:
            print(msg)
            continue

        used_letters.add(guess)
        if guess in word:
            counter = -1
            for letter in word:
                counter += 1
                if guess == letter:
                    word_play[counter] = letter
            print("You got one!")
        else:
            error_counter += 1
        print(f"You have {max_errors - error_counter} mistakes left")
    else:
        print("You won!")
        break
else:
    print("Game Over: too many mistakes")
    print(f"The word was: {word}")
