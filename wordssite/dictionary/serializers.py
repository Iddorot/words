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
    def create(self, validated_data):
        """
        Create and return a new `Word` instance, given the validated data.
        """
        return Word.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Word` instance, given the validated data.
        """
        instance.word = validated_data.get('word', instance.word)
        instance.save()
        return instance

class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation

        exclude = ("word",)
        fields = [
            "translation",
            "language",
        ]


    def create(self, validated_data):
        """
        Create and return a new `Translation` instance, given the validated data.
        """
        return Translation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Translation` instance, given the validated data.
        """
        instance.translation = validated_data.get('translation', instance.translation)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance