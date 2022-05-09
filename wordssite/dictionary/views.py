from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Word,Translation
from .forms import WordForm, TranslationForm



class WordCreateView(CreateView):
    success_url = reverse_lazy('word-list')
    model = Word
    fields = ['word']
    template_name = "add_word.html"

def word_list_view(request):
    context ={}
    context["wordlist"] = Word.objects.all()       
    return render(request, "dictionary_list.html", context)

class WordUpdateView(UpdateView):
    model = Word
    fields = ['word']

class WordDeleteView(DeleteView):
    model = Word
    success_url = reverse_lazy('Word-list')


class TranslationCreateView(CreateView):
    model = Translation
    fields = ['translation', 'language']

class TranslationUpdateView(UpdateView):
    model = Translation
    fields = ['translation', 'language']

class TranslationDeleteView(DeleteView):
    model = Translation
    success_url = reverse_lazy('Translation-list')