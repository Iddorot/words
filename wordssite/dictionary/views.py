from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect

from .models import Word,Translation
from .forms import TranslationForm, WordForm
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
        return render(request, 'dictionary/word_detail.html', context)
    
    def post(self, request, pk):
        WordFormSet = inlineformset_factory(Word, Translation, fields= ('translation', 'language'), extra = 1) 
        word = Word.objects.get(pk=pk)
        formset = WordFormSet(request.POST, instance=word)
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
        word_form = WordForm()
        translation_form = TranslationForm()
        context = {'word_form':word_form,'translation_form':translation_form }       
        return render(request, 'dictionary/word_form.html', context)
    
    def post(self, request):
        word_form = WordForm(request.POST)
        translation_form = TranslationForm(request.POST)
        context = {'word_form':word_form,'translation_form':translation_form } 

        if word_form.is_valid() and translation_form.is_valid():
            word = word_form.save(commit=False)
            word_form.save()
            translation = translation_form.save(commit=False)
            translation.word= word
            translation.save()           
            translation_form.save()
            next = request.POST.get('next', '/dictionary')
            return HttpResponseRedirect(next)
        else:
            print(f"Forms is invalid, errors:\n {word_form.errors}")

        return render(request,'dictionary', context)
    
    """View to create a new Word"""

class WordUpdateView(WordBaseView, UpdateView):
    """View to update a Word"""

class WordDeleteView(WordBaseView, DeleteView):
    """View to translation a Word"""



class TranslationBaseView(View):
    model = Translation
    fields = 'translation', 'language'
    success_url = reverse_lazy('dictionary:all')   

class TranslationUpdateView(TranslationBaseView, UpdateView):
    """View to update a Translation"""

class TranslationDeleteView(TranslationBaseView, DeleteView):
    """View to translation a Translation"""
