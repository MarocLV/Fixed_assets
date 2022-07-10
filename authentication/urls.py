from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateUserView.as_view()),
    path('token/', views.CreateTokenView.as_view())
]