"""Speed test but with module time."""
import sys

sys.path.append("../../../")

from time import time

from palindromes.config import APPLICATION_DATA_DIR
from palindromes.run import run

start = time()
run([
    APPLICATION_DATA_DIR / "american_dict.txt", APPLICATION_DATA_DIR / "names.txt"
])
print(time() - start)
