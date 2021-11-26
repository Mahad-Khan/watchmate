from django.urls import path
# from watchlist_app.api.views import movie_list, movie_detail
# from watchlist_app.api.views import MovieListApiView, MovieDetailApiView
from watchlist_app.api.views import WatchlistApiView, WatchDetailApiView, StreamPlatformListApiView, StreamPlatformDetailApiView

urlpatterns = [
    path('list/', WatchlistApiView.as_view(), name="watch-list"),
    path('list/<int:pk>', WatchDetailApiView.as_view(), name="watch-detail"),

    path('stream/', StreamPlatformListApiView.as_view(), name="stream"),
    path('stream/<int:pk>', StreamPlatformDetailApiView.as_view(), name="stream-detail")
]