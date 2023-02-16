from django import forms
from django.core.exceptions import ValidationError
from .models import Book, Tags


class TagsField(forms.CharField):
    def to_python(self, value: str):
        """
        value == 'python, mysql, django'

        :return: ['python', 'mysql', 'django']
        """
        return list(map(str.strip, value.split(",")))


class BookForm(forms.ModelForm):
    tags = TagsField(widget=forms.TextInput)
    about = forms.CharField(
        required=False, widget=forms.Textarea(attrs={"id": "editor"})
    )

    class Meta:
        model = Book
        fields = ["title", "image", "author", "year", "file", "tags", "about"]

    def save(self, commit=True):
        # До сохранения self.cleaned_data["tags"] имеет тип list[str]
        tags = []
        for tag in self.cleaned_data["tags"]:
            try:
                tag = Tags.objects.get(name__iexact=tag)
            except Tags.DoesNotExist:
                tag = Tags.objects.create(name=tag.lower())
            tags.append(tag)

        # Передаем self.cleaned_data["tags"] имеет тип list[Tags]
        self.cleaned_data["tags"] = tags

        return super().save(commit)
