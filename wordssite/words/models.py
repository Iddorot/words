from django.db import models


class Word(models.Model):
    word_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Translation(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    translation_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)