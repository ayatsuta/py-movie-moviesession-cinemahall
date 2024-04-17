from django.db.models import QuerySet


from db.models import Movie


def get_movies(
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> QuerySet[Movie]:
    query_set = Movie.objects.all()

    if genres_ids:
        query_set = query_set.filter(genres__in=genres_ids)

    if actors_ids:
        query_set = query_set.filter(actors__in=actors_ids)

    return query_set


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> Movie:
    created_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        created_movie.genres.set(genres_ids)
    if actors_ids:
        created_movie.actors.set(actors_ids)
        return created_movie
