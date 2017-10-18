from django.conf.urls import url

from showtime.views import (FederalBodyPage, FederalBodyPageExport,
                            StateBodyPage, StateBodyPageExport, StatePage,
                            StatePageExport)

urlpatterns = [
    url(
        r'^state/(?P<year>\d{4})/(?P<state>[\w-]+)/$',
        StatePage.as_view()
    ),
    url(
        r'^state/(?P<year>\d{4})/(?P<state>[\w-]+)/export/$',
        StatePageExport.as_view()
    ),
    url(
        r'^body/(?P<year>\d{4})/(?P<body>[\w-]+)/$',
        FederalBodyPage.as_view()
    ),
    url(
        r'^body/(?P<year>\d{4})/(?P<body>[\w-]+)/export/$',
        FederalBodyPageExport.as_view()
    ),
    url(
        r'^body/(?P<year>\d{4})/(?P<state>[\w-]+)/(?P<body>[\w-]+)/$',
        StateBodyPage.as_view()
    ),
    url(
        r'^body/(?P<year>\d{4})/(?P<state>[\w-]+)/(?P<body>[\w-]+)/export/$',
        StateBodyPageExport.as_view()
    ),
]
