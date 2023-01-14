from django.contrib import admin
from django.urls import path, include
from .views import Scrapview

urlpatterns = [
    path('scr/',Scrapview.as_view(),name='scrapview')
]
