"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include
from App import views
from App.login_view import login_view
from App.rateMovies_view import rateMovies
from App.interactions_view import interactions
from App.tenmovies_view import tenmovies
from App.remomendMovies_view import recommend_movies
from rest_framework import routers, serializers, viewsets

from App.views import PeliculaViewSet, UserLikeViewSet, knownMovieViewSet, unknownMovieViewSet, gridViewSet, UserViewSet

route = routers.DefaultRouter()

route.register("Pelicula", PeliculaViewSet, basename="Pelicula")
route.register("User", UserViewSet, basename="User")
route.register("knownMovie", knownMovieViewSet, basename="knownMovie")
route.register("unknownMovie", unknownMovieViewSet, basename="unknownMovie")
route.register("gridView", gridViewSet, basename="gridView")
route.register("UserLike", UserLikeViewSet, basename="UserLike")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('api/auth/login', login_view, name='login'),
    path('api/rateMovies', rateMovies, name='rateMovies'),
    path('api/interactions/<int:idUser>/', interactions, name='interactions'),
    path('api/tenmovies/<int:idUser>/', tenmovies, name='tenmovies'),
     path('api/recommend/<int:idUser>/', recommend_movies, name='recommend'),
    path('', views.my_view, name='message-list'),
]
