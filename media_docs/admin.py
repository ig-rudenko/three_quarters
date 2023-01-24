from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


class MediaItemAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "year", "uploaded_by", "show_item", "show_tags"]
    search_fields = ["title", "about", "author"]
    list_filter = ["year"]
    list_per_page = 20

    readonly_fields = ("item_image",)
    fieldsets = (
        (None, {"fields": ("title", "item_image", "image", "file", "about")}),
        ("Создатели", {"fields": ("author", "year", "uploaded_by")}),
        (None, {"fields": ("tags",)}),
    )

    @admin.display(description="Посмотреть")
    def show_item(self, item) -> str:
        return mark_safe(f"<a href=\"{item.get_absolute_url()}\" target=\"_blank\">ссылка</a>")

    @admin.display(description="Теги")
    def show_tags(self, item: models.DocBaseAbstract):

        text = ""
        for tag in item.tags.all():
            text += f"""<p><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-tag" viewBox="0 0 16 16">
                          <path d="M6 4.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm-1 0a.5.5 0 1 0-1 0 .5.5 0 0 0 1 0z"/>
                          <path d="M2 1h4.586a1 1 0 0 1 .707.293l7 7a1 1 0 0 1 0 1.414l-4.586 4.586a1 1 0 0 1-1.414 0l-7-7A1 1 0 0 1 1 6.586V2a1 1 0 0 1 1-1zm0 5.586 7 7L13.586 9l-7-7H2v4.586z"/>
                        </svg>{tag.name}</p>"""

        return mark_safe(text)

    @staticmethod
    def item_image(item: models.DocBaseAbstract):
        return mark_safe(f"<img src=\"{item.image.url}\" style=\"max-height: 300px;\" >")


admin.site.register(
    [
        models.Book,
        models.Journal,
        models.Comics
    ],
    MediaItemAdmin
)

