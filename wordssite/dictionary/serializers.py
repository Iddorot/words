from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from dictionary.models import Word, Translation
from django.conf.global_settings import LANGUAGES

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word

        fields = [
            "word",
        ]

class TranslationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Translation

        exclude = ["word",
        ]
        fields = [
            "translation",
            "language",
        ]
