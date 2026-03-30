from django_filters import FilterSet, ModelChoiceFilter, CharFilter, DateFilter
from .models import Post, Author
from django import forms


class PostFilter(FilterSet):
    post_author = ModelChoiceFilter(queryset=Author.objects.all(), label="Автор", empty_label="Все авторы")
    post_header = CharFilter(label="Заголовок", lookup_expr="iregex")
    post_date = DateFilter(label="Начиная с даты", lookup_expr='gt', widget = forms.DateInput({'type': 'date'}))

