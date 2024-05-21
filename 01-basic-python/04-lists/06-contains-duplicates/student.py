def contains_duplicates(xs):
    no_dupes = set(xs)
    if len(no_dupes) == len(xs):
        return False
    else:
        return True
