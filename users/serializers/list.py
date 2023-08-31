from rest_framework import serializers
from common.helpers import User


class UserListSer(serializers.ModelSerializer):
    class Meta:
        exclude = ['password']
        model = User
