from django.urls import path
from rest_framework.authtoken.models import Token
from rest_framework.authtoken import views          # built-in view to return token
from user_app.api.views import registerations_view, logout_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("login/",views.obtain_auth_token , name="login"),
    path("register/", registerations_view , name="register"),
    path("logout/", logout_view , name="logout"),

    # ### JWT Authentication
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
