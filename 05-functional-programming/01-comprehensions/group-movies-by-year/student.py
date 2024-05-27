def group_movies_by_year(movies):
    return {movie.year: [film.title for film in movies if film.year == movie.year] for movie in movies}