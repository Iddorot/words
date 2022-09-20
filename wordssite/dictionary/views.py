from gettext import translation
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Word, Translation
from .forms import TranslationForm, WordForm, TranslationFormset
from django.shortcuts import render, redirect
from .serializers import WordSerializer, TranslationSerializer

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
    def __init__(self):
        self.WordFormSet = inlineformset_factory(
            Word,
            Translation,
            fields=("translation", "language"),
            extra=1,
            widgets={
                "translation": TextInput(attrs={"placeholder": "Add Translation"})
            },
        )
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
            return HttpResponseRedirect("#")
        else:
            return render(request, "dictionary/word_detail.html", context)


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


@csrf_exempt
def word_list_rest(request):
    """
    List all code words, or create a new word.
    """
    if request.method == 'GET':
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def word_detail_rest(request, pk):
    """
    Retrieve, update or delete a code word.
    """
    try:
        word = Word.objects.get(pk=pk)
    except Word.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = WordSerializer(word,translation)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WordSerializer(word, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        word.delete()
        return HttpResponse(status=204)

class TranslationBaseView(View):
    model = Translation
    fields = "translation", "language"
    success_url = reverse_lazy("dictionary:all")


class TranslationUpdateView(TranslationBaseView, UpdateView):
    """View to update a Translation"""


class TranslationDeleteView(TranslationBaseView, DeleteView):
    """View to delete a Translation"""
