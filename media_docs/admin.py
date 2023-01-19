from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "year", "uploaded_by"]


@admin.register(models.Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "year", "uploaded_by"]


@admin.register(models.Comics)
class ComicsAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "year", "uploaded_by"]
