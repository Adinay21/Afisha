from django.urls import path
from users import views

urlpatterns = [
    path('registration/', views.AuthorizeAPIView.as_view()),
    path('authorization/', views.RegisterAPIView.as_view()),
]