from django.urls import path, include
from .views import CustomUserView, Login, UserView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("user", CustomUserView)

urlpatterns = [   
path('login/',Login.as_view()),
# path("", include(router.urls)),
path('register/',UserView.as_view()),
]