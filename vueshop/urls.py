"""vueshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from user_operation.views import UserFavViewSet, LeavingMessageViewSet, AddressViewSet
from users.views import SmsCodeViewSet, UserViewSet
from vueshop.settings import MEDIA_ROOT
from django.views.static import serve

from goods.views import GoodsViewSet, CategoryViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
# 配置goods的url
router.register(r'goods', GoodsViewSet, base_name='goods')  # views中取消queryset属性，采用get_queryset()方法，则必须加这个

# 配置category的url
router.register(r'categorys', CategoryViewSet, base_name='categorys')

router.register(r'codes', SmsCodeViewSet, base_name='codes')

router.register(r'users',UserViewSet,base_name='users')
# 收藏
router.register(r'userfavs',UserFavViewSet,base_name='userfavs')
# 留言
router.register(r'messages',LeavingMessageViewSet,base_name='messages')
# 收货地址
router.register(r'address',AddressViewSet,base_name='address')


# goods_list = GoodsViewSet.as_view({
#     'get': 'list',
# })

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 直接的图片链接需要配置

    # 商品列表页
    # url(r'goods/$', GoodsListView.as_view(), name="goods-list"),
    # url(r'goods/$', goods_list, name="goods-list"),

    url(r'^', include(router.urls)),

    url(r'docs/', include_docs_urls(title="慕学生鲜")),

    # drf自带的token认证模式,
    # post:username,password
    # return:token(放入请求头中认证)eg:Authorization:Token dcedc19872b67c93b8b43ff8e46481dd5fc4d996
    url(r'^api-token-auth/', views.obtain_auth_token),

    # jwt的认证接口
    url(r'^login/', obtain_jwt_token),
]
