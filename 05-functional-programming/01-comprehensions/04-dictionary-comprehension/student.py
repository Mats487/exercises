def title_to_director(movies):
    return {movie.title: movie.director for movie in movies}


def director_to_titles(movies):
    return {movie.director: [movie_by_director.title for movie_by_director in movies if movie_by_director.director == movie.director] for movie in movies}
