from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from users.serializers.list import UserListSer
from common.helpers import User
from rest_framework import permissions
from rest_framework.decorators import action

from users.serializers.register import RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserListSer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]

    @action(
        methods=['post'],
        detail=False,
        url_path='register',
        serializer_class=RegisterSerializer,
        permission_classes=[AllowAny],
    )
    def register(self, request):
        return super().create(request)
