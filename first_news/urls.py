from django.urls import path
from . import views
from django.contrib import admin


app = 'first_news'
urlpatterns = [
    path('', views.first_object, name='first_object'),
    path('article/<int:pk>/', views.secound_object,name='secound_object'),
    path('article/new/', views.thrd_object, name='thrd_object'),
    path('comment/create/<int:pk>/',views.force_object,name='force_object'),
    ]
