"""Application entry file."""
import os

from .script import palindrome_words_list


def app(file_path: str) -> list:
    """Application entry.

    :return: None
    """
    if not os.path.exists(file_path):
        raise IOError("File not found")
    with open(file_path, "r", encoding="utf-8") as file:
        words_list = file.read().strip().split("\n")
    palindromes = palindrome_words_list(words_list)
    return palindromes
