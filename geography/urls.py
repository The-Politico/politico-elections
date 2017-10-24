from django.conf.urls import include, url
from rest_framework import routers

from .viewsets import DivisionViewSet, StateViewSet

router = routers.DefaultRouter()

router.register(r'divisions', DivisionViewSet)
router.register(r'states', StateViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
