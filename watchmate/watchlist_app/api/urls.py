from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_detail
# from watchlist_app.api.views import MovieListApiView, MovieDetailApiView
from watchlist_app.api.views import (ReviewList, ReviewDetail, ReviewCreate,
                                    WatchlistApiView, WatchDetailApiView, 
                                    #StreamPlatformListApiView, StreamPlatformDetailApiView,
                                    StreamPlatformVS)


router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('watch/', WatchlistApiView.as_view(), name="watch-list"),
    path('watch/<int:pk>/', WatchDetailApiView.as_view(), name="watch-detail"),

    path('', include(router.urls)), # router will handle all types of request
    
        # if we have such type of requirements like list all elements and access each element e.g \
        # stream urls then we can use viewsets with routers

    # path('stream/', StreamPlatformListApiView.as_view(), name="stream"),
    # path('stream/<int:pk>', StreamPlatformDetailApiView.as_view(), name="stream-detail"),

    # path('review/', ReviewList.as_view(), name="review-list"),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail"),

    # path('watch/<int:pk>/review/', ReviewList.as_view(), name="review-list"),    # list all views of a particular movie 
    path('watch/<int:pk>/review/', ReviewDetail.as_view(), name="review-detail"), 
    path('watch/<int:pk>/review-create/', ReviewCreate.as_view(), name="review-create"), # create review for a particular movie

]