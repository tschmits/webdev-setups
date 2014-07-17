from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Note: the weird '*(...)' construct below is a workaround to use the
# single-level indent (as is customary for Django url files) instead
# of a deeper one, as would be typically required.

urlpatterns = patterns('', *(
    url(r'^admin/', include(admin.site.urls)),
))

if settings.DEBUG:
    urlpatterns += patterns('', *(
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}),
    ))
else:
    urlpatterns += patterns('', *(
    ))

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('', *(
        url(r'^jasmine/', include('django_jasmine.urls')),
    ))
