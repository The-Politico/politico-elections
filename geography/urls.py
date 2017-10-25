from django.conf.urls import include, url
from rest_framework import routers

from .viewsets import DivisionViewSet

router = routers.DefaultRouter()

router.register(r'divisions', DivisionViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
