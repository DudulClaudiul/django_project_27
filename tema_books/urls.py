from django.urls import path
from . import views

urlpatterns = [
    path('data/ordered_names', views.ordered_names, name='ordered_names'),
    path('data/ordered_numbers', views.ordered_numbers, name='ordered_numbers'),
    path('data/paired_names', views.paired_names, name='paired_names'),
]