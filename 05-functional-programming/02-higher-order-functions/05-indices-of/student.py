def indices_of(xs, condition):
    return [xs.index(x) for x in xs if condition(x)]