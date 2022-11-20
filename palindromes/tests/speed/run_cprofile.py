import cProfile
from palindromes.run import run
from palindromes.config import APPLICATION_DATA_DIR

cProfile.run('run([APPLICATION_DATA_DIR / "american_dict.txt", APPLICATION_DATA_DIR / "names.txt"])')
