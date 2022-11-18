"""Here app colors."""
from dataclasses import dataclass


@dataclass
class Colors:
    """Class with colors."""

    PINK = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
