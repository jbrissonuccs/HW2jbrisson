from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('booking',views.booking, name='booking'),
    path('account',views.account, name='account'),
    path('movieIndex',views.movieIndex, name='movieIndex'),
    path('new_show',views.new_show, name='new_show'),
]