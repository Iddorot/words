from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory

from .models import Word,Translation
from .forms import TranslationForm
from django.shortcuts import render, redirect





class WordBaseView(View):
    model = Word
    fields = '__all__'
    success_url = reverse_lazy('dictionary:all')

class WordListView(WordBaseView, ListView):
    """View to list all Word"""

class WordDetailView(WordBaseView, UpdateView):

    def get(self, request, pk):
        WordFormSet = inlineformset_factory(Word, Translation, fields= ('translation', 'language'), extra = 1)
        word = Word.objects.get(pk=pk)
        formset = WordFormSet(instance=word,queryset=Word.objects.none())
        context = {'formset':formset, 'word': word}

        if request.method == 'POST':
            formset = WordFormSet(request.POST)
            
            if formset.is_valid():
                for form in formset:
                    form=TranslationForm(request.POST)
                    translation = form.save(commit=False)
                    word = Word.objects.get(pk=pk)
                    translation.word= word
                    translation.save()
                form=TranslationForm()
                return redirect('dictionary/word_detail.html', context)
        
        return render(request, 'dictionary/word_detail.html', context)

    """View to list the details from one Word"""

class WordCreateView(WordBaseView, CreateView):
    """View to create a new Word"""

class WordUpdateView(WordBaseView, UpdateView):
    """View to update a Word"""

class WordDeleteView(WordBaseView, DeleteView):
    """View to translation a Word"""



class TranslationBaseView(View):
    model = Translation
    fields = 'translation', 'language'
    success_url = reverse_lazy('dictionary:all')   


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
    """View to translation a Translation"""
