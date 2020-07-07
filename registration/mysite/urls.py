from django.urls import path
from .import views
from .views import CourList, CourDetail, CourUpdate, CourDelete, CourCreate
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views




urlpatterns = [

   
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    
    
    path('home', CourList.as_view(), name='cour-index'),
    path('cour-detail/<int:pk>/', CourDetail.as_view(), name='cour-detail'),
    path('cour-update/<int:pk>/', CourUpdate.as_view(), name='cour-update'),
    path('cour-delete/<int:pk>/', CourDelete.as_view(), name='cour-delete'),
    path('cour-create', CourCreate.as_view(), name='cour-create'),
    
     
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration1/password_change_done.html'), 
        name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration1/password_change.html'), 
        name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration1/password_reset_done.html'),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration1/password_reset_form.html'), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration1/password_reset_complete.html'),
     name='password_reset_complete'),

]

