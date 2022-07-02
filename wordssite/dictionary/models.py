import datetime
import uuid
from django.db import models
from django.utils import timezone
from django.conf.global_settings import LANGUAGES
import random

    
class UUIDBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)


    class Meta:
        abstract = True
    

class Word(UUIDBaseModel):
    word= models.CharField(max_length=200)

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        return reverse('word', kwargs={'pk': self.pk})

    def get_random():
        list_all_words = list(Word.objects.values('word'))
        number_of_objects = Word.objects.count()
        num = 10
        if number_of_objects < num :
            random_words = random.sample(list_all_words, number_of_objects)
        else:
            random_words = random.sample(list_all_words, num)

        return random_words

class Translation(UUIDBaseModel):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    translation= models.CharField(max_length=200)
    language = models.CharField(max_length=7, choices=LANGUAGES)


    def __str__(self):
        return self.translation
        
