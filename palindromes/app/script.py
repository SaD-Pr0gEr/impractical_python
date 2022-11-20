"""Here are the functions that define the palindrome."""


def palindrome_checker(word: str) -> bool:
    """Palindrome words checker.

    Function accepts word and returns palindrome status

    :return: bool
    """
    return word == word[::-1] and len(word) > 1


def palindrome_words_list(words_list: list) -> list:
    """Palindrome words.

    Program reads file and returns a list of palindrome words

    :return: list
    """
    palindromes = []
    for word in words_list:
        if palindrome_checker(word):
            palindromes.append(word)
    return palindromes
