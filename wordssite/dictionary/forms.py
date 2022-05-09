from django import forms
from .models import Word,Translation
 
 
class WordForm(forms.ModelForm):
 
    class Meta:
        model = Word
 
        fields = [
            "word",
        ]

class TranslationForm(forms.ModelForm):
 
    class Meta:
        model = Translation
 
        fields = [
            "translation",
            "language",
        ]
