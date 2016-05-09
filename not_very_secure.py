import re

def alphanumeric(string):
    pattern = re.compile(r"\w+$")

    if pattern.match(string):
        return True
    else:
        return False


test = alphanumeric("")
print test
