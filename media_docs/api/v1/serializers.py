from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ...models import Book, Tags
from user.models import User


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ["name"]

    def validate_name(self, value: str):
        if value.isdigit():
            raise ValidationError("Тег не должен быть числом!")
        return value


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "hobby"]


class BookSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True)
    user = serializers.CharField(source="uploaded_by.username", read_only=True)

    class Meta:
        model = Book
        exclude = ["file", "about", "uploaded_by"]


class DetailBookSerializer(BookSerializer):
    file_size = serializers.CharField(read_only=True)
    user = UserSerializer(source="uploaded_by")

    class Meta:
        model = Book
        fields = "__all__"


class UserBooksSerializer(serializers.ModelSerializer):
    book_set = BookSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "hobby", "book_set"]
