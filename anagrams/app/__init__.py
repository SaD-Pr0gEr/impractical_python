"""Application entry file."""
import os

from .script import check_anagram_word


def app(file_path: str, word_input: str) -> list:
    """Application entry function.

    :return: list
    """
    anagrams_list = []
    if not os.path.exists(file_path):
        raise IOError("File not found")
    with open(file_path, "r", encoding="utf-8") as file:
        words_list = file.read().strip().split("\n")
    for word in words_list:
        if word != word_input and check_anagram_word(word_input, word):
            anagrams_list.append(word)
    return anagrams_list
