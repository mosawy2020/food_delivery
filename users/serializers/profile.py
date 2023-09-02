from users.serializers.list import UserListSer


class ProfileSerializer(UserListSer):
    class Meta(UserListSer.Meta):
        read_only_fields = [
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',]
