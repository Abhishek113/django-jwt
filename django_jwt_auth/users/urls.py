from django.conf.urls import url
from django.urls import path
from .views import CreateUserAPIView, UserRetriveUpdateAPIView, authenticate_user


urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('obtain_token/', authenticate_user),
    path('update/', UserRetriveUpdateAPIView.as_view()),
]