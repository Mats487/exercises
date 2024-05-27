def titles(movies):
    return [movie.title for movie in movies]


def titles_and_years(movies):
    titles = [movie.title for movie in movies]
    years = [movie.year for movie in movies]
    return list(zip(titles, years))


def titles_and_actor_counts(movies):
    titles = [movie.title for movie in movies]
    actors = [len(movie.actors) for movie in movies]
    return list(zip(titles, actors))


def reverse_words(senctence):
    return " ".join([word[::-1] for word in senctence.split()])
