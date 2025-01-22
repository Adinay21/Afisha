from django.urls import path
from movie_app import views


urlpatterns = [
    path('movie/', views.MovieListCreateAPIView.as_view()),
    path('movie/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('director/', views.DirectorListCreateAPIView.as_view()),
    path('director/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('review/', views.ReviewListCreateAPIView.as_view()),
    path('review/<int:id>/', views.ReviewDetailAPIView.as_view()),
]