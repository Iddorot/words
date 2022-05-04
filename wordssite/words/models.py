import datetime

from django.db import models
from django.utils import timezone

class Word(models.Model):
    word_text = models.CharField(max_length=200)
    word_translation = models.CharField(max_length=200, default='DEFAULT VALUE')
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.word_text
        def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text