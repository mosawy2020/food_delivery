from django.contrib import admin
from django.urls import path
from rest_framework import routers

from users.viewsets.user import UserViewSet
from django.urls import include
router = routers.DefaultRouter()
router.register(prefix='users', viewset=UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
