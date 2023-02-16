from django.urls import path, include
from django.views.generic import TemplateView
from . import views

# /api/v1/

urlpatterns = [
    path("books/", views.ListBookAPIView.as_view()),
    path("book/<int:book_id>", views.DetailBookAPIView.as_view()),

    path("tags/", views.TagsListCreateAPIView.as_view()),

    path("user/<int:user_id>/books", views.UserBookAPIView.as_view())
]
