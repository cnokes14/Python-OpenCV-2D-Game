import time
import random
from os import path

# This function returns time in ms, as an int.
def get_time_ms():
    return int(round(time.time() * 1000))

# This function is just random.randint(), but
#   checks if min and max are the same first.
def rintrange(min : int, max : int):
    if min == max:
        return min
    return random.randint(min, max)

# This just gets the location of the project directory.
#   This assumes that this file is only one subfolder deep.
_dir = path.dirname(path.dirname(__file__))
def get_fpath():
    return _dir