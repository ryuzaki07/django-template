from django.urls import path

from . import views

urlpatterns = [
    path('api/all-chats', views.GetChats, name="all-chats"),
    path('api/create-chats', views.CreateChats, name="create-chats"),
]
