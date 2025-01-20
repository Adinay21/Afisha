from django.urls import path
from movie_app import views


urlpatterns = [
    path('movie/', views.movie_list_api_view),
    path('movie/<int:id>/', views.movie_detail_list_api_view),
    path('director/', views.director_list_api_view),
    path('director/<int:id>/', views.director_detail_list_api_view),
    path('review/', views.review_list_api_view),
    path('review/<int:id>/', views.review_detail_list_api_view)
]