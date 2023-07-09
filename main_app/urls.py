from django.urls import path
from . import views
from .models import Movie, Director

urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('about/', views.About.as_view(), name = "About"),
    path('movies/', views.MovieList.as_view(), name ="Movies"),
    path('movies/new/', views.MovieCreate.as_view(), name="movie_create"),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name='movie_detail'),
    path('movies/<int:pk>/update', views.MovieUpdate.as_view(), name='movie_update'),
    path('movies/<int:pk>/delete',views.MovieDelete.as_view(), name="movie_delete"),
    path('movies/<int:pk>/directors/new/', views.DirectorCreate.as_view(), name="director_create"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]
    

        


