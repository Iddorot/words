from django import template
from dictionary.models import Word
import random

register = template.Library()

@register.simple_tag
def get_random():
    items = list(Word.objects.all())
    number_of_objects = len(items)
    num = 10
    if number_of_objects < num :
        for i in range(number_of_objects):
            random_item = random.choice(items)
            return random_item
    else:
        for i in range(num):
            random_item = random.choice(items)
            return random_item


