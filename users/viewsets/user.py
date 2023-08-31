from rest_framework import viewsets
from users.serializers.list import UserListSer
from common.helpers import User
from rest_framework import permissions


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserListSer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]
