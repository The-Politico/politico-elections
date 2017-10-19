from django.conf.urls import url

from showtime.views import (CyclePage, CyclePageExport, FederalBodyPage,
                            FederalBodyPageExport, FederalExecutiveRacePage,
                            FederalExecutiveRacePageExport, LinkPreview,
                            StateBodyPage, StateBodyPageExport,
                            StateExecutiveRacePage,
                            StateExecutiveRacePageExport, StateFedPage,
                            StateFedPageExport, StatePage, StatePageExport)

urlpatterns = [
    url(r'^$',
        LinkPreview.as_view(),
        name='preview'
    ),
    url(
        r'^cycle/(?P<year>\d{4})/$',
        CyclePage.as_view(),
        name='cycle-page'
    ),
    url(
        r'^cycle/(?P<year>\d{4})/export/$',
        CyclePageExport.as_view(),
        name='cycle-page-export'
    ),
    url(
        r'^state/(?P<year>\d{4})/(?P<state>[\w-]+)/$',
        StatePage.as_view(),
        name='state-page'
    ),
    url(
        r'^state/(?P<year>\d{4})/(?P<state>[\w-]+)/export/$',
        StatePageExport.as_view(),
        name='state-page-export'
    ),
    url(
        r'^state/(?P<year>\d{4})/(?P<branch>[\w-]+)/(?P<state>[\w-]+)/$',
        StateFedPage.as_view(),
        name='state-fed-page'
    ),
    url(
        r'^state/(?P<year>\d{4})/(?P<branch>[\w-]+)/(?P<state>[\w-]+)/export/$', # noqa
        StateFedPageExport.as_view(),
        name='state-fed-page-export'
    ),
    url(
        r'^body/(?P<year>\d{4})/(?P<body>[\w-]+)/$',
        FederalBodyPage.as_view(),
        name='fed-body-page'
    ),
    url(
        r'^body/(?P<year>\d{4})/(?P<body>[\w-]+)/export/$',
        FederalBodyPageExport.as_view(),
        name='fed-body-page-export'
    ),
    url(
        r'^body/(?P<year>\d{4})/(?P<state>[\w-]+)/(?P<body>[\w-]+)/$',
        StateBodyPage.as_view(),
        name='state-body-page'
    ),
    url(
        r'^body/(?P<year>\d{4})/(?P<state>[\w-]+)/(?P<body>[\w-]+)/export/$',
        StateBodyPageExport.as_view(),
        name='state-body-page-export'
    ),
    url(
        r'^race/(?P<year>\d{4})/(?P<office>[\w-]+)/$',
        FederalExecutiveRacePage.as_view(),
        name='fed-exec-race-page'
    ),
    url(
        r'^race/(?P<year>\d{4})/(?P<office>[\w-]+)/export/',
        FederalExecutiveRacePageExport.as_view(),
        name='fed-exec-race-page-export'
    ),
    url(
        r'^race/(?P<year>\d{4})/(?P<state>[\w-]+)/(?P<office>[\w-]+)/$',
        StateExecutiveRacePage.as_view(),
        name='state-exec-race-page'
    ),
    url(
        r'^race/(?P<year>\d{4})/(?P<state>[\w-]+)/(?P<office>[\w-]+)/export/',
        StateExecutiveRacePageExport.as_view(),
        name='state-exec-race-page-export'
    ),
]
