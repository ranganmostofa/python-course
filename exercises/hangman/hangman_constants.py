from enum import Enum


class GuessValidationCode(Enum):
    SUCCESS = 0
    ALPHA_ERROR = 1
    LENGTH_ERROR = 2
    ALREADY_USED_ERROR = 3


GUESS_VALIDATION_CODE_MAP = {
    GuessValidationCode.SUCCESS: "",
    GuessValidationCode.ALPHA_ERROR: "Please enter a letter",
    GuessValidationCode.LENGTH_ERROR: "Please enter only one letter",
    GuessValidationCode.ALREADY_USED_ERROR: "You already guessed that",
}
