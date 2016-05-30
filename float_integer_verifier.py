import re

def i_or_f(arr):

    pattern = re.compile("[+,-]?\d*\.?([e, E][+,-]?)?\d*$")

    if pattern.match(arr):
        return True
    else:
        return False
