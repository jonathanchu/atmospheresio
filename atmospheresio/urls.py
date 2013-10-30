from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='home.html')),

    # Examples:
    # url(r'^$', 'atmospheresio.views.home', name='home'),
    # url(r'^atmospheresio/', include('atmospheresio.foo.urls')),

    # content
    url(r'^statusboard/', include('statusboard.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
