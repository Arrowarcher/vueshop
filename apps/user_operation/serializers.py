from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from user_operation.models import UserFav


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