import datetime
import uuid
from django.db import models
from django.utils import timezone
from django.conf.global_settings import LANGUAGES

    
class UUIDBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)


    class Meta:
        abstract = True
    
    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                (field.verbose_name, 
                Genre.objects.get(pk=field.value_from_object(self)).name)
                for field in self.__class__._meta.fields[1:]
            ]

class Word(UUIDBaseModel):
    word= models.CharField(max_length=200)

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        return reverse('word', kwargs={'pk': self.pk})


class Translation(UUIDBaseModel):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    translation= models.CharField(max_length=200)
    language = models.CharField(max_length=7, choices=LANGUAGES)


    def __str__(self):
        return self.translation

    def get_absolute_url(self):
        return reverse('translatiom', kwargs={'pk': self.pk})
