def contains_duplicates(xs):
    if len(xs) == len(set(xs)):
        return False
    else:
        return True
