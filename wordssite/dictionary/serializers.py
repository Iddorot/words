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
    word = WordSerializer()
    class Meta:
        model = Translation

        fields = [
            "word",
            "translation",
            "language",
        ]

    def create(self, validated_data):
        wordObject = Word.objects.get(self.word)
        instance = Translation.objects.create(**validated_data)
        Translation.objects.create(Word=wordObject, Translation=instance)
        return instance
        
