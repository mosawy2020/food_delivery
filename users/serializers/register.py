from rest_framework import serializers
from common.helpers import User, validated
from common.validaors import Confirmed


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True, validators=[Confirmed(other_field='password')])

    class Meta:
        model = User
        fields = ["first_name", 'last_name', 'email', 'is_active', 'password', 'confirm_password']

    def create(self, validated_data):
        validated_data = validated(validated_data, except_these=['confirm_password'])
        return User.objects.create(**validated_data)
