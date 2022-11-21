"""Application entry(runner) file."""

from pathlib import Path
from typing import List, Union

from app import app
from config import APPLICATION_DATA_DIR


def run(file_paths: List[Union[str, Path]]):
    """Application runner."""
    word_input = input("Input your word: ")
    for path in file_paths:
        anagrams = app(path, word_input)
        print(anagrams)


if __name__ == "__main__":
    run([
        APPLICATION_DATA_DIR / "american_dict.txt",
        APPLICATION_DATA_DIR / "names.txt"
    ])
