from django import forms
from .models import Word, Translation
from django.core.exceptions import ValidationError


class WordForm(forms.ModelForm):
    def clean_word(self):
        word = self.cleaned_data["word"].title()

        if Word.objects.filter(word=word).exists():
            raise ValidationError(f"{word} already exist")

        if not word.isalpha():
            raise ValidationError("Please only enter letters")

        return word

    class Meta:
        model = Word

        fields = [
            "word",
        ]


class TranslationForm(forms.ModelForm):
    def clean_translation(self):
        translation = self.cleaned_data["translation"].title()
        print(Translation.word)
        if Translation.objects.filter(translation=translation).exists():
            print("this transtion exist")
            raise ValidationError(f"{translation} already exist")

        if any(str.isdigit(i) for i in translation):
            print("Please enter letters")
            raise ValidationError("Please enter letters")

        return translation

    class Meta:
        model = Translation
        exclude = ("word",)
        fields = [
            "translation",
            "language",
        ]
