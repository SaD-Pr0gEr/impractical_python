"""Here script(-s) for working with anagrams."""


def check_anagram_word(user_input_word: str, check_word: str) -> bool:
    """Check anagram word.

    :return: bool
    """
    sorted_word_list = sorted(user_input_word.lower())
    sorted_check_word_list = sorted(check_word.lower())
    return sorted_word_list == sorted_check_word_list
