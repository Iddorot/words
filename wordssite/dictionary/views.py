from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect

from .models import Word, Translation
from .forms import TranslationForm, WordForm
from django.shortcuts import render, redirect



class WordBaseView(View):
    model = Word
    fields = '__all__'
    success_url = reverse_lazy('dictionary:all')


class WordListView(WordBaseView, ListView):
    """View to list all Word"""

class WordDetailView(WordBaseView, UpdateView):
    def __init__(self):
        self.WordFormSet = inlineformset_factory(Word, Translation, fields= ('translation', 'language'), extra = 1)
    
    def get(self, request, pk):
        word = Word.objects.get(pk=pk)
        formset = self.WordFormSet(instance=word,queryset=Word.objects.none())
        context = {'formset':formset, 'word': word}
        return render(request, 'dictionary/word_detail.html', context)
    
    def post(self, request, pk):
        word = Word.objects.get(pk=pk)
        formset = self.WordFormSet(request.POST, instance=word)
        context = {'formset':formset, 'word': word}
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("")

        else:
            print(f"Formset is invalid, errors:\n {formset.errors}")

        return render(request,'dictionary/word_detail.html', context)

    """View to list the details from one Word"""

class WordCreateView(WordBaseView, CreateView):   
    def get(self, request):
        form = WordForm()
        translation_form = TranslationForm()
        context = {'form':form,'translation_form':translation_form }       
        return render(request, 'dictionary/word_form.html', context)
    
    def post(self, request):
        form = WordForm(request.POST)
        translation_form = TranslationForm(request.POST)
        context = {'form':form,'translation_form':translation_form }

        if form.is_valid() and translation_form.is_valid():
            word= form.save(commit=False)
            form.save()
            translation = translation_form.save(commit=False)
            translation.word= word
            translation.save()           
            translation_form.save()
            next = request.POST.get('next', '/dictionary')
            return HttpResponseRedirect(next)
        else:
            print(f"Forms are invalid, errors:\n {form.errors}")

        return render(request,'dictionary/word_form.html', context)
    
    """View to create a new Word"""

class WordUpdateView(WordBaseView, UpdateView):

    """View to update a Word"""

class WordDeleteView(WordBaseView, DeleteView):
    """View to delete a Word"""



class TranslationBaseView(View):
    model = Translation
    fields = 'translation', 'language'
    success_url = reverse_lazy('dictionary:all')   

class TranslationUpdateView(TranslationBaseView, UpdateView):
    """View to update a Translation"""

class TranslationDeleteView(TranslationBaseView, DeleteView):
    """View to delete a Translation"""
