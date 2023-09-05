from rest_framework import serializers
from common.helpers import User, validated
from common.validaors import Confirmed, Same


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True, validators=[Same(other_field="password")])

    class Meta:
        model = User
        fields = ["first_name", 'last_name', 'email', 'is_active', 'password', 'confirm_password']

    def create(self, validated_data):
        validated_data = validated(data=validated_data, except_these=['confirm_password'])
        return super().create(validated_data)
