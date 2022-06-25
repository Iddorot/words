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
 
    def get_random(self):
        max_id = Word.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            word = Word.objects.filter(pk=pk).first()
            if word:
                return word



class Translation(UUIDBaseModel):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    translation= models.CharField(max_length=200)
    language = models.CharField(max_length=7, choices=LANGUAGES)


    def __str__(self):
        return self.translation