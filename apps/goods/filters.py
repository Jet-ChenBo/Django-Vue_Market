import django_filters
from .models import Goods
from django.db.models import Q

class GoodsFilter(django_filters.rest_framework.FilterSet):
    '''
    商品的过滤器
    '''
    pricemin = django_filters.NumberFilter(field_name='shop_price', lookup_expr='gte')
    pricemax = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        queryset = queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))
        return queryset

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax']
