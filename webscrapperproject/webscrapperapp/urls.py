from django.urls import path

from . import views
from django import urls

urlpatterns = [
    path('',views.home,name='home')]