from django_filters import FilterSet, CharFilter, NumberFilter

from ..models import Product


class ProductFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', distinct=True)
    category = CharFilter(field_name='category__name',
                          lookup_expr='icontains', distinct=True)
    max_price = CharFilter(
        lookup_expr='lte', distinct=True, field_name='price')
    min_price = CharFilter(
        lookup_expr='gte', distinct=True, field_name='price')

    class Meta:
        model = Product
        fields = [
            'min_price',
            'max_price',
            'category',
            'name',
            'description',
        ]
