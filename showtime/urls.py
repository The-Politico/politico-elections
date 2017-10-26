from django.conf.urls import include, url

from showtime.views import (CyclePage, CyclePageExport, FederalBodyPage,
                            FederalBodyPageExport, FederalExecutiveRacePage,
                            FederalExecutiveRacePageExport, LinkPreview,
                            StateBodyPage, StateBodyPageExport,
                            StateExecutiveRacePage,
                            StateExecutiveRacePageExport, StateFedPage,
                            StateFedPageExport, StatePage, StatePageExport)

from .viewsets import (BodyDetail, BodyList, ElectionDayDetail,
                       ElectionDayList, OfficeDetail, OfficeList, StateDetail,
                       StateList)

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
        r'^race/(?P<year>\d{4})/(?P<office>[\w-]+)/export/$',
        FederalExecutiveRacePageExport.as_view(),
        name='fed-exec-race-page-export'
    ),
    url(
        r'^race/(?P<year>\d{4})/(?P<state>[\w-]+)/(?P<office>[\w-]+)'
        r'/(?P<date>\d{4}-\d{2}-\d{2})/$',
        StateExecutiveRacePage.as_view(),
        name='state-exec-race-page'
    ),
    url(
        r'^race/(?P<year>\d{4})/(?P<state>[\w-]+)/(?P<office>[\w-]+)'
        r'/(?P<date>\d{4}-\d{2}-\d{2})/export/',
        StateExecutiveRacePageExport.as_view(),
        name='state-exec-race-page-export'
    ),
    #############
    # API VIEWS #
    #############
    url(
        r'^api/elections/$',
        ElectionDayList.as_view(),
        name='election-list',
    ),
    url(
        r'^api/elections/(?P<date>\d{4}-\d{2}-\d{2})/$',
        ElectionDayDetail.as_view(),
        name='election-detail',
    ),
    url(
        r'^api/elections/(?P<date>\d{4}-\d{2}-\d{2})/states/$',
        StateList.as_view(),
        name='state-election-list',
    ),
    url(
        r'^api/elections/(?P<date>\d{4}-\d{2}-\d{2})/states/(?P<pk>.+)/$',
        StateDetail.as_view(),
        name='state-election-detail',
    ),
    url(
        r'^api/elections/(?P<date>\d{4}-\d{2}-\d{2})/bodies/$',
        BodyList.as_view(),
        name='body-election-list',
    ),
    url(
        r'^api/elections/(?P<date>\d{4}-\d{2}-\d{2})/bodies/(?P<pk>.+)/$',
        BodyDetail.as_view(),
        name='body-election-detail',
    ),
    url(
        r'^api/elections/(?P<date>\d{4}-\d{2}-\d{2})/executive-offices/$',
        OfficeList.as_view(),
        name='office-election-list',
    ),
    url(
        r'^api/elections/(?P<date>\d{4}-\d{2}-\d{2})/'
        'executive-offices/(?P<pk>.+)/$',
        OfficeDetail.as_view(),
        name='office-election-detail',
    ),
]
