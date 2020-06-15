from django.urls import path
from . import views
from .views import CourList, CourDetail
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    #path('home', views.home, name='home'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('password_reset', views.password_reset, name='password_reset'),
    path('home', CourList.as_view(), name='cour-index'),
    path('cour-detail/<int:pk>/', CourDetail.as_view(), name='cour-detail'),
]
