from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from goods.serializers import GoodsSerializer
from user_operation.models import UserFav, UserLeavingMessage


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        fields = ('user','goods','id')
        validators = [                  # model里设置了这边就不用设置了，一样的
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user','goods'),
                message='已经收藏'
            )
        ]

class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ('goods', 'id')


class LeavingMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )           # 直接获取当前的用户，这样前端传进来的用户相关操作，无需再加用户id
    add_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = UserLeavingMessage
        fields = ('user', 'message_type','subject','message','file','id','add_time')