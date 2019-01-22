from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('change_password/', views.change_password, name='change_password'),
   #path('reset_password_email', views.reset_password_email, name='reset_password_email'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    url('^', include('django.contrib.auth.urls')),
    path('custom_user/', views.custom_user, name='custom_user'),
]

