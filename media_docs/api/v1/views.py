from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from user.models import User
from .serializers import BookSerializer, DetailBookSerializer, TagsSerializer, UserBooksSerializer
from ...models import Book, Tags


class ListBookAPIView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class DetailBookAPIView(APIView):

    def get(self, request, book_id: int):
        book = get_object_or_404(Book, id=book_id)
        serializer = DetailBookSerializer(book)
        return Response(serializer.data)


class TagsListCreateAPIView(APIView):

    def get(self, request):
        tags = Tags.objects.all()
        serializer = TagsSerializer(tags, many=True)
        return Response(serializer.data)

    def put(self, request):
        print(type(request.data), request.data)

        serializer = TagsSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        print(serializer.validated_data)

        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class UserBookAPIView(APIView):

    def get(self, request, user_id: int):
        user = get_object_or_404(User, id=user_id)
        serializer = UserBooksSerializer(user)
        return Response(serializer.data)
