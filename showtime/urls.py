from django.conf.urls import url

from showtime.views import (FederalBodyPage, FederalBodyPageExport, StatePage,
                            StatePageExport)

urlpatterns = [
    url(r'^state/(\d{4})/([\w-]+)/$', StatePage.as_view()),
    url(r'^state/(\d{4})/([\w-]+)/export/$', StatePageExport.as_view()),
    url(r'^body/(\d{4})/([\w-]+)/$', FederalBodyPage.as_view()),
    url(r'^body/(\d{4})/([\w-]+)/export/$', FederalBodyPageExport.as_view()),
]
