from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import stringformat
from django.views import View

from .filters import MediaDocsFiler
from .models import Book, Journal, Comics
from .forms import BookForm


class DisplayViewBase(View):
    queryset = None
    category = ""
    type = ""
    image = ""

    def get(self, request):

        return render(
            request,
            "items_list.html",
            {
                "items": MediaDocsFiler(request.GET, self.queryset).qs.order_by("-created"),
                "available_years": self.queryset.values("year").distinct(),
                "image": "img/books.png",
                "category": {
                    "name": self.category,
                    "type": self.type,
                    "image": self.image
                },
            },
        )


class BooksViewBase(DisplayViewBase):
    queryset = Book.objects.all().select_related("uploaded_by")
    category = "Книги"
    type = "books"
    image = "img/books.png"


class JournalsViewBase(DisplayViewBase):
    queryset = Journal.objects.all().select_related("uploaded_by")
    category = "Статьи"
    type = "journal"
    image = "img/journal.png"


class ComicsViewBase(DisplayViewBase):
    queryset = Comics.objects.all().select_related("uploaded_by")
    category = "Комиксы"
    type = "comics"
    image = "img/comics.png"


class DetailBookView(View):
    def get(self, request, book_slug: str):
        return render(
            request,
            "show_item.html",
            {
                "item": get_object_or_404(Book, slug=book_slug),
            },
        )


class DetailJournalView(View):
    def get(self, request, journal_slug: str):
        return render(
            request,
            "show_item.html",
            {
                "item": get_object_or_404(Journal, slug=journal_slug),
            },
        )


class DetailComicsView(View):
    def get(self, request, comics_slug: str):
        return render(
            request,
            "show_item.html",
            {
                "item": get_object_or_404(Comics, slug=comics_slug),
            },
        )


class CreateBookView(View):

    def get(self, request):
        form = BookForm()
        return render(request, "create_form.html", {"form": form})

    def post(self, request):
        book = Book(uploaded_by=request.user)
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            # Просто Form
            # Book.objects.create(
            #     **form.cleaned_data, uploaded_by=request.user
            # )

            # ModelForm
            form.save()  # сохраняем в БАЗУ

            return redirect("books")

        return render(request, "create_form.html", {"form": form})


class UpdateBookView(View):

    def get(self, request, slug: str):
        book = get_object_or_404(Book, slug=slug)
        form = BookForm(instance=book)
        return render(request, "create_form.html", {"form": form})

    def post(self, request, slug: str):
        book = get_object_or_404(Book, slug=slug)
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()

            return redirect("show-book", book_slug=slug)

        return render(request, "create_form.html", {"form": form})
