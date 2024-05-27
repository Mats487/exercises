def take_while(xs, condition):
    i = 0
    while i < len(xs) and condition(xs[i]):
        i += 1
    return (xs[:i], xs[i:])



def is_negative(x):
    return x < 0


print(take_while([-4, -2, -2, -1, -4, -6], is_negative))
