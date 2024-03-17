from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('search/', views.search_thesis, name='search_thesis'),
    path('thesis/<int:thesis_id>/comment/', views.add_comment, name='add_comment'),
]