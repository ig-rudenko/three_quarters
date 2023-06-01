from django.views import generic
from .models import Book, Journal, Comics


class DetailItemView(generic.DetailView):
    slug_url_kwarg = "item_slug"
    context_object_name = "item"
    template_name = "show_item.html"


class ListItemView(generic.ListView):
    template_name = "items_list.html"
    context_object_name = "items"
    queryset = Book.objects.all().select_related("uploaded_by")
    image = ""
    category_name = ""

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(
            object_list=object_list, image=self.image, category=self.category_name
        )


class BooksView(ListItemView):
    queryset = Book.objects.all().select_related("uploaded_by")
    image = "img/books.png"
    category_name = "Книги"


class DetailBookView(DetailItemView):
    model = Book


class JournalView(ListItemView):
    queryset = Journal.objects.all().select_related("uploaded_by")
    image = "img/journal.png"
    category_name = "Журналы"


class DetailJournalView(DetailItemView):
    model = Journal


class ComicsView(ListItemView):
    queryset = Comics.objects.all().select_related("uploaded_by")
    image = "img/comics.png"
    category_name = "Комиксы"


class DetailComicsView(DetailItemView):
    model = Comics
