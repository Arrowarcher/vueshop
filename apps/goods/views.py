from rest_framework import generics, mixins, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from goods.filters import GoodsFilter
from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response     # 比Django的强大

from .models import Goods

class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100

class GoodsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页，分页，搜索，排序
    """

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    pagination_class = GoodsPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)    # 记得，否则没有过滤器按钮
    # filter_fields = ('name', 'shop_price')
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'add_time')
    # '^' 以指定内容开始.
    # '=' 完全匹配
    # '@' 全文搜索（目前只支持Django的MySQL后端）
    # '$' 正则搜索

    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get('price_min', 0)
    #     if price_min:
    #         queryset = queryset.filter(shop_price__gt=int(price_min))
    #     return  queryset

    # def get(self, request, *args, **kwargs):
    #     print(111)
    #     return self.list(request, *args, **kwargs)

    # def get(self, request, format=None):
    #     goods = Goods.objects.all()[:10]
    #     goods_serializer = GoodsSerializer(goods, many=True)        # 类似Django的forms，但是可以序列化为json
    #     return Response(goods_serializer.data)
