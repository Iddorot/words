from django.urls import path, reverse, include
from . import views
from django.views.generic.base import TemplateView
from rest_framework import routers

app_name = "dictionary"

router = routers.DefaultRouter()
router.register(r'words', views.WordViewSet)
router.register(r'translations', views.TranslationViewSet)

urlpatterns = [
    path("", views.WordHomeView.as_view(template_name="home.html"), name="home"),
    path("dictionary/", views.WordListView.as_view(), name="all"),
    path(
        "dictionary/<uuid:pk>/detail",
        views.WordDetailView.as_view(),
        name="word_detail",
    ),
    path("dictionary/create/", views.WordCreateView.as_view(), name="word_create"),
    path(
        "dictionary/<uuid:pk>/update/",
        views.WordUpdateView.as_view(),
        name="word_update",
    ),
    path(
        "dictionary/<uuid:pk>/delete/",
        views.WordDeleteView.as_view(),
        name="word_delete",
    ),
    path(
        "dictionary/translation/<uuid:pk>/update/",
        views.TranslationUpdateView.as_view(),
        name="translation_update",
    ),
    path(
        "dictionary/translation/<uuid:pk>/delete/",
        views.TranslationDeleteView.as_view(),
        name="translation_delete",
    ),
    path(
        '', include(router.urls)
    ),
    path(
        'api-auth/', include('rest_framework.urls', 
        namespace='rest_framework')
    )
]
