import re


def starts_with_a(string):
    return re.fullmatch('a.*', string)
