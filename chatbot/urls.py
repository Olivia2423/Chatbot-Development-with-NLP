from django.urls import path
from . import views

##1.
urlpatterns = [
    path ('', views.chatbot, name= 'chatbot'), ##1. specifies what path, 2. render the chatbot from the views
    path ('login', views.login, name='login'),
    path ('register', views.register, name='resgister'),
    path ('logout', views.logout, name='logout')
]