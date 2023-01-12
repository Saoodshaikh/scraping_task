from django.contrib import admin
from django.urls import path, include
from .views import scrap
urlpatterns = [

    path('scr',scrap.as_view(),'scarp'),
]
