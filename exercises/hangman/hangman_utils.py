from typing import List, Set, Tuple

from hangman_constants import GuessValidationCode


def _is_valid_word(word: str) -> bool:
    return (
        # Filter out proper nouns
        word[0].islower()
        # Filter out words longer than 5 letters
        and len(word) <= 5
    )


def choose_word(words: Set[str]) -> str:
    while not _is_valid_word(choice := words.pop()):
        continue
    return choice


def validate_guess(guess: str, used_letters: Set[str]) -> GuessValidationCode:
    code = GuessValidationCode.SUCCESS
    # Filter out non-alphabetic guesses
    if not guess.isalpha():
        code = GuessValidationCode.ALPHA_ERROR
    # Filter out guesses longer than 1
    elif len(guess) > 1:
        code = GuessValidationCode.LENGTH_ERROR
    # Filter out guesses already used
    elif guess in used_letters:
        code = GuessValidationCode.ALREADY_USED_ERROR
    return code


def show_progress(word_play: List[str]) -> None:
    print(" ".join(word_play))

