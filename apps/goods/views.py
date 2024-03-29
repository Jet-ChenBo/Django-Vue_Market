from rest_framework import generics
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .serializers import GoodsSerializer, CategorySerializer
from .models import Goods, GoodsCategory
from .filters import GoodsFilter

class GoodsPagination(PageNumberPagination):
    page_size = 12  # 每页多少个
    page_size_query_param = 'page_size'  # 可在url上指定每页多少个
    page_query_param = 'p'  # 设置查询参数为p，例如?p=2  表示第二页
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    商品列表页
    '''
    queryset = Goods.objects.all() # 指定查询集
    serializer_class = GoodsSerializer  # 指定序列化类
    pagination_class = GoodsPagination  # 指定分页类

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # 过滤器
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')  # 搜索
    ordering_fields = ('sold_num', 'shop_price')  # 排序


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        商品分类列表数据
    '''
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer