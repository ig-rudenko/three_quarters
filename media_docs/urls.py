from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),


    path("books/create", views.CreateBookView.as_view(), name="create-book"),
    path("books/<slug:book_slug>", views.DetailBookView.as_view(), name="show-book"),
    path("books/<slug:slug>/update", views.UpdateBookView.as_view(), name="update-book"),
    path("books/", views.BooksViewBase.as_view(), name="books"),

    path("journal/<slug:journal_slug>", views.DetailJournalView.as_view(), name="show-journal"),
    path("journal/", views.JournalsViewBase.as_view(), name="journal"),

    path("comics/<slug:comics_slug>", views.DetailComicsView.as_view(), name="show-comics"),
    path("comics/", views.ComicsViewBase.as_view(), name="comics"),
]
