"""Application init."""

import random
from collections import defaultdict
from pprint import pprint

from .colors import Colors
from .data.names import group_1, group_2


def random_fullname_generator() -> None:
    """
    Random fullname generator.

    :return: None
    """
    print("Добро пожаловать в бессмысленную программу "
          "по генерации бессмысленных имён!")
    while True:
        f_name = random.choice(group_1)
        l_name = random.choice(group_2)
        print(f"{Colors.YELLOW}{f_name} {l_name}")
        try_again = input(f"{Colors.PINK}Попробовать ещё?(y/n): ").lower()
        if try_again == "n":
            print(f"{Colors.RED}Пока!")
            break


def project_pig_latin() -> None:
    """Practice: Program pig latin.

    User inputs word.
    If its starts with 'vowel' letter program endures to
        the end and adds to the end of this word 'ay'.
    If its starts with 'consonant' letter program just adds to
        the end of this word 'way'.

    :return: None
    """
    vowels = "aiueo"

    while True:
        user_word = input("Write some word: ").lower()
        if user_word[0] in vowels:
            print(f"{Colors.GREEN}{user_word}way")
        else:
            print(f"{Colors.YELLOW}{user_word[1:]}{user_word[0]}ay")
        try_again = input(f"{Colors.PINK}Try again?(y/n): ").lower()
        if try_again == "n":
            print(f"{Colors.RED}Bye!")
            break


def pauper_columnar_graphic() -> None:
    """Pauper columnar graphic.

    Pauper inputs sentence.
    Program prints list of letters and the count of letter

    :return: None
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    column_dict = defaultdict(list)
    while True:
        user_sentence = input("Write some sentence: ").replace(" ", "")
        for letter in user_sentence:
            if letter in alphabet:
                column_dict[letter].append(letter)
        print(Colors.GREEN, end="")
        pprint(column_dict)
        try_again = input(f"{Colors.PINK}Try again?(y/n): ").lower()
        if try_again == "n":
            print(f"{Colors.RED}Bye!")
            break
