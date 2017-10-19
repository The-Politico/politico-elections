from django.conf.urls import url

from showtime.views import (CyclePage, FederalBodyPage, FederalBodyPageExport,
                            FederalExecutiveRacePage,
                            FederalExecutiveRacePageExport, StateBodyPage,
                            StateBodyPageExport, StateExecutiveRacePage,
                            StateExecutiveRacePageExport, StateFedPage,
                            StateFedPageExport, StatePage, StatePageExport)

urlpatterns = [
    url(
        r'^cycle/(?P<year>\d{4})/$',
        CyclePage.as_view()
    ),
    url(
        r'^state/(?P<year>\d{4})/(?P<state>[\w-]+)/$',
        StatePage.as_view()
    ),
    url(
        r'^state/(?P<year>\d{4})/(?P<state>[\w-]+)/export/$',
        StatePageExport.as_view()
    ),
    url(
        r'^state/(?P<year>\d{4})/(?P<branch>[\w-]+)/(?P<state>[\w-]+)/$',
        StateFedPage.as_view()
    ),
    url(
        r'^state/(?P<year>\d{4})/(?P<branch>[\w-]+)/(?P<state>[\w-]+)/export/$', # noqa
        StateFedPageExport.as_view()
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
    url(
        r'^race/(?P<year>\d{4})/(?P<office>[\w-]+)/$',
        FederalExecutiveRacePage.as_view()
    ),
    url(
        r'^race/(?P<year>\d{4})/(?P<office>[\w-]+)/export/',
        FederalExecutiveRacePageExport.as_view()
    ),
    url(
        r'^race/(?P<year>\d{4})/(?P<state>[\w-]+)/(?P<office>[\w-]+)/$',
        StateExecutiveRacePage.as_view()
    ),
    url(
        r'^race/(?P<year>\d{4})/(?P<state>[\w-]+)/(?P<office>[\w-]+)/export/',
        StateExecutiveRacePageExport.as_view()
    ),
]
