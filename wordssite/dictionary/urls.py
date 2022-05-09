from django.urls import path, reverse
from . import views


urlpatterns = [
    path('word/add/', views.WordCreateView.as_view(), name='word-add'),
    path('word/list/', views.word_list_view, name='word-list'),
    path('word/<int:pk>/', views.WordUpdateView.as_view(), name='word-update'),
    path('word/<int:pk>/delete/', views.WordDeleteView.as_view(), name='word-delete'),
]
