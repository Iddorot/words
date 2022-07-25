from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Word, Translation
from .forms import TranslationForm, WordForm, TranslationFormset
from django.shortcuts import render, redirect


class WordBaseView(View):
    model = Word
    fields = "__all__"
    success_url = reverse_lazy("dictionary:all")


class WordListView(WordBaseView, ListView):
    """View to list all Word"""


class WordHomeView(WordBaseView, ListView):
    def get(self, request):
        random_words = Word.get_random()
        context = {"random_words": random_words}
        return render(request, "home.html", context)


class WordDetailView(WordBaseView, UpdateView):

    def get(self, request, pk):
        word = Word.objects.get(pk=pk)
        formset = TranslationFormset(instance=word, queryset=Word.objects.none())
        context = {"formset": formset, "word": word}
        return render(request, "dictionary/word_detail.html", context)

    def post(self, request, pk):
        word = Word.objects.get(pk=pk)
        formset = TranslationFormset(request.POST, instance=word)
        context = {"formset": formset, "word": word,}
        if formset.is_valid():
            formset.save()
        print(formset.non_form_errors())
        return HttpResponseRedirect("")


class WordCreateView(WordBaseView, CreateView):
    def get(self, request):
        form = WordForm()
        translation_form = TranslationForm()
        context = {"form": form, "translation_form": translation_form}
        return render(request, "dictionary/word_form.html", context)

    def post(self, request):
        form = WordForm(request.POST)
        translation_form = TranslationForm(request.POST)
        context = {"form": form, "translation_form": translation_form}

        if form.is_valid() and translation_form.is_valid():
            word = form.save(commit=False)
            form.save()
            translation = translation_form.save(commit=False)
            translation.word = word
            translation.save()
            next = request.POST.get("next", "/dictionary")
            return HttpResponseRedirect(next)
        return render(request, "dictionary/word_form.html", context)


class WordUpdateView(WordBaseView, UpdateView):
    """View to update a Word"""


class WordDeleteView(WordBaseView, DeleteView):
    """View to delete a Word"""


class TranslationBaseView(View):
    model = Translation
    fields = "translation", "language"
    success_url = reverse_lazy("dictionary:all")


class TranslationUpdateView(TranslationBaseView, UpdateView):
    """View to update a Translation"""


class TranslationDeleteView(TranslationBaseView, DeleteView):
    """View to delete a Translation"""
