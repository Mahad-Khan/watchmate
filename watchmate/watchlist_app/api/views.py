from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies)