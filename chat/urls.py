# urls.py
from django.urls import path
from .views import chat_view

urlpatterns = [
    path('users/', chat_view, name='user_list'),
]