from django.urls import path,include
from django.contrib import admin


app = 'first_news'
urlpatterns = [
    path('',include('first_news.urls'))
    ]
