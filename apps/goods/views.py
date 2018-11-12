from rest_framework import generics, mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import  DjangoFilterBackend

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
    商品列表页
    """

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend,)    # 记得，
    # filter_fields = ('name', 'shop_price')
    filter_class = GoodsFilter
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
