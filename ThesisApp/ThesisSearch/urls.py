from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_thesis, name='search_thesis'),
]