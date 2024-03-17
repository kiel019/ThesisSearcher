from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_thesis, name='search_thesis'),
    path('thesis/<int:thesis_id>/comment/', views.add_comment, name='add_comment'),
]