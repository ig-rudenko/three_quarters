from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Book, Journal, Comics


class BooksView(View):
    def get(self, request):
        return render(
            request,
            "items_list.html",
            {
                "items": Book.objects.all().select_related("uploaded_by"),
                "image": "img/books.png",
                "category": "Книги",
            },
        )


class DetailBookView(View):
    def get(self, request, book_slug: str):
        book = get_object_or_404(Book, slug=book_slug)
        return render(
            request,
            "show_item.html",
            {
                "item": book,
            },
        )


class JournalView(View):
    def get(self, request):
        return render(
            request,
            "items_list.html",
            {
                "items": Journal.objects.all().select_related("uploaded_by"),
                "image": "img/journal.png",
                "category": "Статьи"
            },
        )


class DetailJournalView(View):
    def get(self, request, journal_slug: str):
        journal = get_object_or_404(Journal, slug=journal_slug)
        return render(
            request,
            "show_item.html",
            {
                "item": journal,
            },
        )