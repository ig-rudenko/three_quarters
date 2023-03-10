import django_filters
from django.db.models import Q


class MediaDocsFiler(django_filters.FilterSet):

    search = django_filters.CharFilter(method="search_filter")
    author = django_filters.CharFilter(lookup_expr="icontains")
    year = django_filters.NumberFilter()
    tags = django_filters.CharFilter(field_name="tags__name")

    @staticmethod
    def search_filter(queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(about__icontains=value)
        )
