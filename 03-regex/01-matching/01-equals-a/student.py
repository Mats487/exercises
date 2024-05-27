import re


def equals_a(string):
    if re.fullmatch('a', string):
        return True
    else:
        return False
