from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.serializers.list import UserListSer
from common.helpers import User
from rest_framework import permissions
from rest_framework.decorators import action

from users.serializers.profile import ProfileSerializer
from users.serializers.register import RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserListSer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        if self.action in ['retrieve_profile', 'update_profile', 'change_password']:
            return self.request.user
        return super().get_object()
    @action(
        methods=['post'],
        detail=False,
        url_path='register',
        serializer_class=RegisterSerializer,
        permission_classes=[AllowAny],
    )
    def register(self, request):
        return super().create(request)
    @action(
        methods=['get'],
        detail=False,
        url_path='profile',
        serializer_class=ProfileSerializer,
        permission_classes=[AllowAny],
    )
    def retrieve_profile(self, request):
        return super().retrieve(request)
    @action(
        methods=['put'],
        detail=False,
        url_path='change-password',
        serializer_class=ChangePasswordSerializer,
        permission_classes=[IsAuthenticated],
    )
    def change_password(self, request):
        return super().update(request)