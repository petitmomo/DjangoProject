from django.urls import path
from . import views

urlpatterns = [

    path('home', views.home, name='home'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('password_reset', views.password_reset, name='password_reset'),

]
