from django import forms
from .models import Flashcard

class NewFlashCardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        exclude = ('author', 'created', 'updated',)