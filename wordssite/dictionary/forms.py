from django import forms
from .models import Word,Translation
from django.core.exceptions import ValidationError
 
 
class WordForm(forms.ModelForm):
    def clean_word(self):
        word = self.cleaned_data["word"]
        if Word.objects.filter(word = word).count()>0:
            raise ValidationError(f"{word} already exist")

        return word
    class Meta:
        model = Word
 
        fields = [
            "word",
        ]
        

class TranslationForm(forms.ModelForm):
 
    class Meta:
        model = Translation

        exclude = ("word", )
        fields = [
            "translation",
            "language",
        ]
