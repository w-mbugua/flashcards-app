from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('add.html',views.add, name="add"),
    path('subtract.html',views.subtract, name="subtract"),
    path('multiply.html',views.multiply, name="multiply"),
    path('divide.html',views.divide, name="divide"),
=======

from .views import home, createcards

urlpatterns = [ 
    path('', home, name='home'),
    path('new/', createcards, name='new_card'),
>>>>>>> a36329b8d3981bc1dd868d27b838690c2ddbb514
]