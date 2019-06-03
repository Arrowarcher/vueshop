from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user_operation.models import UserFav
from user_operation.serializers import UserFavSerializer
from utils.permissions import IsOwnerOrReadOnly


class UserFavViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin):
    """
    用户收藏功能
    """
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)       # 用户需登录,所有者
    serializer_class = UserFavSerializer
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    lookup_field = 'goods_id'

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

