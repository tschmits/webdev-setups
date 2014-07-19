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

    # this overrides the url with a custom template
    url(r'^accounts/signin/$', 'userena.views.signin', {
        'template_name': 'accounts/signin_form.html'}, name="signin"),
    url(r'^accounts/', include('userena.urls')),
))


if settings.DEBUG:
    urlpatterns += patterns('', *(
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}),
    ))
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('', *(
        url(r'^jasmine/', include('django_jasmine.urls')),
    ))
