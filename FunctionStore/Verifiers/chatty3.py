import string
from typing import Tuple


class InputVerifier:
    def __init__(self, valid_chars: str, type_text: str, empty_allowed: bool = False):
        self.valid_chars = valid_chars
        self.type_text = type_text
        self.empty_allowed = empty_allowed

    def check_unwanted_chars(self, text: str) -> bool:
        """
        Checks if the given text contains any unwanted characters.
        """
        for char in text:
            if char not in self.valid_chars:
                return True
        return False

    def prompt_input(self, invalid_message: Tuple[str, str] = None) -> str:
        """
        Prompts the user for input and handles validation messages.
        """
        if not self.empty_allowed:
            message = invalid_message[0] if invalid_message else f"You gave an EMPTY value!\nPlease enter a {self.type_text}: "
        else:
            message = invalid_message[1] if invalid_message else f"'{text}' is NOT A {self.type_text}!\nPlease enter a {self.type_text}: "

        while True:
            text = input(message)
            if text or self.empty_allowed:
                return text

    def verify(self, text: str, invalid_message: Tuple[str, str] = None) -> str:
        """
        Verifies the given text based on the valid characters and type.
        """
        while True:
            if not text and not self.empty_allowed:
                text = self.prompt_input(invalid_message)
            elif self.check_unwanted_chars(text):
                text = self.prompt_input(invalid_message=("Your input contains invalid characters!",))
            else:
                return text


def main():
    valid_int_chars = "-+0123456789"
    valid_float_chars = "-+0123456789."
    valid_alpha_chars = string.ascii_letters
    valid_punc_chars = string.punctuation
    valid_all_chars = string.printable.replace("a", "")

    verifier = InputVerifier(valid_float_chars, "float number")
    user = verifier.verify(input("Using InputVerifier to check Only Float numbers: ").strip())
    print(("empty" if not user else user), "is valid")

    verifier = InputVerifier(valid_int_chars, "integer number")
    user = verifier.verify(input("Using InputVerifier to check Only integer numbers: ").strip())
    print(("empty" if not user else user), "is valid")

    verifier = InputVerifier(valid_float_chars, "negative number", empty_allowed=True)
    user = verifier.verify(input("Using InputVerifier to check Only Negative Numbers: ").strip())
    print(("empty" if not user else user), "is valid")

    # Additional similar usage examples...


if __name__ == '__main__':
    main()