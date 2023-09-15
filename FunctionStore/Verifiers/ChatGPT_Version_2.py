import string
from typing import Tuple


def check_unwanted_chars(text: str, valid_chars: str) -> bool:
    """
    Checks if the given text contains any unwanted characters.
    """
    for char in text:
        if char not in valid_chars:
            return True
    return False


def prompt_input(type_text: str, invalid_message: Tuple[str, str] = None, empty_allowed=False) -> str:
    """
    Prompts the user for input and handles validation messages.
    """
    if not empty_allowed:
        message = invalid_message[0] if invalid_message else (
            f"You gave an EMPTY value!\nPlease enter a {type_text}: "
        )
    else:
        message = invalid_message[1] if invalid_message else (
            f"'{text}' is NOT A {type_text}!\nPlease enter a {type_text}: "
        )
    
    while True:
        text = input(message)
        if text or empty_allowed:
            return text


def verify(text: str, valid_chars: str, type_text: str, empty_allowed=False) -> str:
    """
    Verifies the given text based on the valid characters and type.
    """
    while True:
        if not text and not empty_allowed:
            text = prompt_input(type_text, empty_allowed=empty_allowed)
        elif check_unwanted_chars(text, valid_chars):
            text = prompt_input(
                type_text, invalid_message=("Your input contains invalid characters!",),
                empty_allowed=empty_allowed
            )
        else:
            return text


def main():
    valid_int_chars = "-+0123456789"
    valid_float_chars = "-+0123456789."
    valid_alpha_chars = string.ascii_letters
    valid_punc_chars = string.punctuation
    valid_all_chars = string.printable.replace("a", "")

    user = verify(
        input("Using verify to check Only Float numbers: ").strip(),
        valid_float_chars,
        "float number"
    )
    print(("empty" if not user else user), "is valid")

    user = verify(
        input("Using verify to check Only integer numbers: ").strip(),
        valid_int_chars,
        "integer number"
    )
    print(("empty" if not user else user), "is valid")

    user = verify(
        input("Using verify to check Only Negative Numbers: ").strip(),
        valid_float_chars,
        "negative number",
        only_negative=True
    )
    print(("empty" if not user else user), "is valid")

    user = verify(
        input("Using verify to check Only Positive Numbers: ").strip(),
        valid_float_chars,
        "positive number",
        only_positive=True
    )
    print(("empty" if not user else user), "is valid")

    user = verify(
        input("Using verify to check Only Negative Integer: "),
        valid_int_chars,
        "negative integer",
        only_negative=True,
        invalid_message=("Come on, You didn't give a value!", "Come on, a Negative Integer!")
    )
    print(("empty" if not user else user), "is valid")

    user = verify(
        input("Using verify to check Only letters: "),
        valid_alpha_chars,
        "letter",
        empty_allowed=False,
        invalid_message=(
            "No Not an empty value!",
            "Your input contains invalid characters that are not letters"
        ),
        ignore=(".", ",", "!", " ")
    )
    print(("empty" if not user else user), "is valid")

    user = verify(
        input("Using verify to check Only Punctuations: "),
        valid_punc_chars,
        "punctuation",
        empty_allowed=True,
        ignore=" "
    )
    print(("empty" if not user else user), "is valid")

    user = verify(
        input("Using verify to check All characters (Nothing really!!): "),
        valid_all_chars,
        "character",
        every=True,
        invalid_message=("No empty value please", "How can you be wrong?!"),
        remove=("a")
    )
    print(("empty" if not user else user), "is valid")


if __name__ == '__main__':
    main()
