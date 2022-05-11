from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Word,Translation




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