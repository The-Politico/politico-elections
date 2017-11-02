from django.conf.urls import include, url
from rest_framework import routers

from .viewsets import ElectionViewSet, PartyViewSet

router = routers.DefaultRouter()

router.register(r'elections', ElectionViewSet)
router.register(r'parties', PartyViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
