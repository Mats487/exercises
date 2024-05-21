def drop_nth(xs, n):
    first_half = xs[:n]
    last_half = xs[n+1:]
    return [*first_half, *last_half]
