from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from dictionary.models import Word, Translation
from django.conf.global_settings import LANGUAGES

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word

        fields = [
            "word",
        ]

class TranslationSerializer(serializers.HyperlinkedModelSerializer):
    word = serializers.CharField(read_only=True)
    class Meta:
        model = Translation

        fields = [
            "word",
            "translation",
            "language",
        ]
        
