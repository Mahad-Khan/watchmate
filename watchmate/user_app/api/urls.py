from django.urls import path
from rest_framework.authtoken.models import Token
from rest_framework.authtoken import views          # built-in view to return token

urlpatterns = [
    path("login/",views.obtain_auth_token , name="login"),
]
