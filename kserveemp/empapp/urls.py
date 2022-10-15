from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('submit-sentiment/', submit_sentiment, name='submit-sentiment'),
    path('questions/', questions_page, name='questions'),
]