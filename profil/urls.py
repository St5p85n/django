from django.urls import path
from .views import addUtilisateur,deconnexion,connexion
from rest_framework_simplejwt import views as jwttoken
urlpatterns = [
    path('register/',addUtilisateur,name='register'),
    path('logout/',deconnexion,name='logout'),
    path('login/',connexion,name='login'),
    path('connexion/',jwttoken.TokenObtainPairView.as_view(),name="connexion"),
    path('token/refresh/',jwttoken.TokenRefreshView.as_view(),name="token_refresh"),
]