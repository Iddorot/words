from django.urls import path, reverse, re_path
from . import views

app_name = 'dictionary'

urlpatterns = [
    path('', views.WordListView.as_view(), name='all'),
    path('dictionary/<uuid:pk>/detail', views.WordDetailView.as_view(), name='word_detail'),
    path('dictionary/create/', views.WordCreateView.as_view(), name='word_create'),
    path('dictionary/<uuid:pk>/update/', views.WordUpdateView.as_view(), name='word_update'),
    path('dictionary/<uuid:pk>/delete/', views.WordDeleteView.as_view(), name='word_delete'),
]