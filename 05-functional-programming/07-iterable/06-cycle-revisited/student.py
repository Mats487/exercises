def cycle(values):
    values = list(values)
    while True:
        for value in values:
            yield value