from django.db import models
from django.template.defaultfilters import slugify

from user.models import User


def item_file_name(instance: "ItemBase", filename: str):
    return "/".join([instance.__class__.__name__.lower(), instance.slug, filename])


class ItemBase(models.Model):
    title = models.CharField(max_length=255, unique=True)
    about = models.TextField()
    author = models.CharField(max_length=100)
    file = models.FileField(upload_to=item_file_name)
    year = models.IntegerField()
    slug = models.SlugField(blank=True, unique=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(
        User, related_name="%(class)s", on_delete=models.SET_NULL, null=True
    )
    image = models.ImageField(upload_to=item_file_name)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(
            self.title.translate(
                str.maketrans(
                    r"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                    r"abvgdeejzijklmnoprstufhc4ss_y_euaABVGDEEJZIJKLMNOPRSTUFHC4SS_Y_EUA",
                )
            )
        )
        return super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True


class Book(ItemBase):

    def get_absolute_url(self):
        return "/books/" + self.slug


class Journal(ItemBase):

    def get_absolute_url(self):
        return "/journal/" + self.slug


class Comics(ItemBase):

    def get_absolute_url(self):
        return "/comics/" + self.slug
