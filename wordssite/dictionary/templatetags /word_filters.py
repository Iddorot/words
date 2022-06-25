from django import template
#from django.template.defaultfilters import stringfilter
from wordssite.dictionary.models import Word

register = template.Library()


# def get_random():
#     max_id = Word.objects.all().aggregate(max_id=Max("id"))['max_id']
#     while True:
#         pk = random.randint(1, max_id)
#         word = Word.objects.filter(pk=pk).first()
#         if word:
#             return word.word
@register.simple_tag
def total_word():
    return Word.objects.count()