from django.urls import path
from . import views
from .views import home, createcards

urlpatterns = [
    path('',views.home, name="home"),
    path('add.html',views.add, name="add"),
    path('subtract.html',views.subtract, name="subtract"),
    path('multiply.html',views.multiply, name="multiply"),
    path('divide.html',views.divide, name="divide"),
    path('', home, name='home'),
    path('new/', createcards, name='new_card'),
]
