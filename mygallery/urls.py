from django.urls import path
from .views import welcome
from django.conf.urls import url

from . import views


urlpatterns = [
    path('',welcome, name='home'),
    url(r'^search/', views.search_results, name='search_results')