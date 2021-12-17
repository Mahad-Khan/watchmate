from django.urls import path
from rest_framework.authtoken.models import Token
from rest_framework.authtoken import views          # built-in view to return token
from user_app.api.views import registerations_view, logout_view

urlpatterns = [
    path("login/",views.obtain_auth_token , name="login"),
    path("register/", registerations_view , name="register"),
    path("logout/", logout_view , name="logout")
]
