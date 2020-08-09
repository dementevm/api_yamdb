from django_filters import CharFilter, FilterSet

from .models import Titles


class TitlesFilter(FilterSet):
    category = CharFilter(field_name='category__slug', lookup_expr='iexact')
    genre = CharFilter(field_name='genre__slug', lookup_expr='iexact')
    name = CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Titles
        fields = ['category', 'genre', 'year', 'name']
