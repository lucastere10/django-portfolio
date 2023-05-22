import django_filters
from django_filters import CharFilter, ChoiceFilter
from django import forms
from .models import *

class PostFilter(django_filters.FilterSet):
    headline = CharFilter(field_name='headline', lookup_expr='icontains', label="")
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(), widget = forms.CheckboxSelectMultiple, label = "")
    class Meta:
        model = Post
        fields = ['headline', 'tags']
