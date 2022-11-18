"""Application init."""

import random

from .colors import Colors
from .data.names import group_1, group_2


def app() -> None:
    """
    Application runner.

    :return: None
    """
    print("Добро пожаловать в бессмысленную программу по генерации бессмысленных имён!")
    while True:
        f_name = random.choice(group_1)
        l_name = random.choice(group_2)
        print(f"{Colors.YELLOW}{f_name} {l_name}")
        try_again = input(f"{Colors.PINK}Попробовать ещё?(y/n): ").lower()
        if try_again == "n":
            print(f"{Colors.RED}Пока!")
            break
