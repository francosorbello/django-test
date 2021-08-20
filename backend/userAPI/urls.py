from django.urls import path

from userAPI.views import UserAPIView

urlpatterns = [
    path('user-api/',UserAPIView.as_view()),
    path('user-api/<int:pk>/',UserAPIView.as_view()),
]