from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views.gauges import traffic


urlpatterns = patterns(
    '',

    # gauges
    url(r'^gauges.json$', traffic, name='gauges'),
    url(r'^gauges/$', traffic, name='gauges'),
)
