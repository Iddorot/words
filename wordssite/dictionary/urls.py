from django.urls import path, reverse
from . import views

app_name = 'dictionary'

urlpatterns = [
    path('', views.WordListView.as_view(), name='all'),
    path('dictionary/<uuid:pk>/detail', views.WordDetailView.as_view(), name='word_detail'),
    path('dictionary/create/', views.WordCreateView.as_view(), name='word_create'),
    path('dictionary/<uuid:pk>/update/', views.WordUpdateView.as_view(), name='word_update'),
    path('dictionary/<uuid:pk>/delete/', views.WordDeleteView.as_view(), name='word_delete'),
<<<<<<< HEAD
    
    path('dictionary/translation/<uuid:pk>/update/', views.TranslationUpdateView.as_view(), name='translation_update'),
    path('dictionary/translation/<uuid:pk>/delete/', views.TranslationDeleteView.as_view(), name='translation_delete'),
]
||||||| parent of 58c287c (add update, delete and add new one to translation list)

    path('', views.TranslationListView.as_view(), name='all'),
    path('dictionary/<uuid:pk>/detail', views.TranslationDetailView.as_view(), name='translation_detail'),
    path('dictionary/create/', views.TranslationCreateView.as_view(), name='translation_create'),
    path('dictionary/<uuid:pk>/update/', views.TranslationUpdateView.as_view(), name='translation_update'),
    path('dictionary/<uuid:pk>/delete/', views.TranslationDeleteView.as_view(), name='translation_delete'),
]
=======

    path('', views.TranslationListView.as_view(), name='all'),
    path('dictionary/translation/create/', views.TranslationCreateView.as_view(), name='translation_create'),
    path('dictionary/translation/<uuid:pk>/update/', views.TranslationUpdateView.as_view(), name='translation_update'),
    path('dictionary/translation/<uuid:pk>/delete/', views.TranslationDeleteView.as_view(), name='translation_delete'),
]
>>>>>>> 58c287c (add update, delete and add new one to translation list)
