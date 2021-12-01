from django.urls import path
# from watchlist_app.api.views import movie_list, movie_detail
# from watchlist_app.api.views import MovieListApiView, MovieDetailApiView
from watchlist_app.api.views import (ReviewList, ReviewDetail, ReviewCreate,
                                    WatchlistApiView, WatchDetailApiView, 
                                    StreamPlatformListApiView, StreamPlatformDetailApiView)

urlpatterns = [
    path('watch/', WatchlistApiView.as_view(), name="watch-list"),
    path('watch/<int:pk>', WatchDetailApiView.as_view(), name="watch-detail"),

    path('stream/', StreamPlatformListApiView.as_view(), name="stream"),
    path('stream/<int:pk>', StreamPlatformDetailApiView.as_view(), name="stream-detail"),

    path('review/', ReviewList.as_view(), name="review-list"),
    path('review/<int:pk>', ReviewDetail.as_view(), name="review-detail"),

    path('watch/<int:pk>/review', ReviewList.as_view(), name="review-list"),    # list all views of a particular movie 
    path('watch/review/<int:pk>', ReviewDetail.as_view(), name="review-detail"),
    path('watch/<int:pk>/review-create', ReviewCreate.as_view(), name="review-create"), 

]