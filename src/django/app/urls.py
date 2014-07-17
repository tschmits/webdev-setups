from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Note: the weird '*(...)' construct below is a workaround to use the
# single-level indent (as is customary for Django url files) instead
# of a deeper one, as would be typically required.

urlpatterns = patterns('', *(
    url(r'^preview_data/$', 'omtip.publisher.views.preview_data',
        name='preview_data'),
    url(r'^preview/$', 'omtip.publisher.views.preview',
        name='preview'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
))

if settings.DEBUG:
    urlpatterns += patterns('', *(
        url(r'^$', 'omtip.publisher.views.viewer'),
        url(r'^embed/$', 'omtip.publisher.views.viewer_embed'),
        url(r'^dashboard/$', 'omtip.publisher.views.viewer4'),
        url(r'^embed/dashboard/$', 'omtip.publisher.views.viewer4_embed'),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}),
    ))
else:
    urlpatterns += patterns('', *(
        url(r'^$', 'omtip.publisher.views.require_static'),
    ))

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('', *(
        url(r'^jasmine/', include('django_jasmine.urls')),
    ))
