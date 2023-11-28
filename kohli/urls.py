from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.login, name='login'),
    path('chat', views.chatbot, name='chatbot'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
]