def directors(movies):
    return {movie.director for movie in movies}


def common_elements(xs, ys):
    return {value for value in xs if value in ys}
