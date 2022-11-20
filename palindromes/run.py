"""Application runner."""
from pathlib import Path
from typing import List, Union

from palindromes.app import app
from .config import APPLICATION_DATA_DIR


def run(file_paths: List[Union[str, Path]]):
    """Application runner."""
    for path in file_paths:
        palindromes = app(path)
        print(palindromes)


if __name__ == "__main__":
    run([APPLICATION_DATA_DIR / "american_dict.txt", APPLICATION_DATA_DIR / "names.txt"])
