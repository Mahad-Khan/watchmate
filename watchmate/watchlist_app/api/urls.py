from django.urls import path
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import MovieListApiView, MovieDetailApiView

urlpatterns = [
    path('list/', MovieListApiView.as_view(), name="movie_list"),
    path('<int:pk>', MovieDetailApiView.as_view(), name="movie_detail")
]