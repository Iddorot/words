from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Word,Translation
from .forms import TranslationForm
from django.shortcuts import render




class WordBaseView(View):
    model = Word
    fields = '__all__'
    success_url = reverse_lazy('dictionary:all')

class WordListView(WordBaseView, ListView):
    """View to list all Word"""

class WordDetailView(WordBaseView, DetailView):
    """View to list the details from one Word"""

class WordCreateView(WordBaseView, CreateView):
    """View to create a new Word"""

class WordUpdateView(WordBaseView, UpdateView):
    """View to update a Word"""

class WordDeleteView(WordBaseView, DeleteView):
    """View to delete a Word"""



class TranslationBaseView(View):
    model = Translation
    fields = 'translation', 'language'
    success_url = reverse_lazy('dictionary:all')   

class TranslationListView(TranslationBaseView, ListView):
    """View to list all Translation"""


class TranslationCreateView(TranslationBaseView, CreateView):
    def post(self, request, pk):
        if request.method == 'POST':
            form=TranslationForm(request.POST)
            if form.is_valid():
                translation = form.save(commit=False)
                word = Word.objects.get(pk=pk)
                translation.word= word
                translation.save()
        form=TranslationForm()
        return render(request,'dictionary/word_detail.html', {'form':form, 'word':word})   
    """View to create a new Translation"""

class TranslationUpdateView(TranslationBaseView, UpdateView):
    """View to update a Translation"""

class TranslationDeleteView(TranslationBaseView, DeleteView):
    """View to delete a Translation"""
