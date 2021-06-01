from django.urls import path

from .views import home, createcards

urlpatterns = [ 
    path('', home, name='home'),
    path('new/', createcards, name='new_card'),
]