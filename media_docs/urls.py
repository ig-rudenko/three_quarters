from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html")),
    path("books/<slug:book_slug>", views.DetailBookView.as_view(), name="show-book"),
    path("books/", views.BooksView.as_view(), name="books"),

    path("journal/<slug:journal_slug>", views.DetailJournalView.as_view(), name="show-journal"),
    path("journal/", views.JournalView.as_view(), name="journal"),
]
