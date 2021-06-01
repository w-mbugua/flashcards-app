from django.contrib import admin
from .models import Category, Flashcard


admin.site.register(Flashcard)
admin.site.register(Category)