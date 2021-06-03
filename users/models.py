from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Flashcard(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cards")
    title = models.CharField(max_length=50)
    note = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


