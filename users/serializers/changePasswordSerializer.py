from rest_framework import serializers

from common.validaors import Confirmed, Exists
from common.helpers import User
from django.contrib.auth.password_validation import validate_password
from typing import Dict, Any
from django.core.validators import ValidationError


class ChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True,
                                         validators=[validate_password]
                                         )
    confirm_new_password = serializers.CharField(write_only=True, validators=[Confirmed(other_field='new_password')])
    old_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'old_password',
            'new_password',
            'confirm_new_password',
        ]

    def validate_old_password(self, value):
        request_user = getattr(self.context.get('request'), 'user', None)
        if not request_user.check_password(value):
            raise ValidationError('Old password is not correct')
        return value

    def update(self, instance, validated_data):
        instance.password = validated_data.get('new_password')
        instance.save()
        return instance