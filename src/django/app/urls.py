from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('', *(

    url(r'^$', TemplateView.as_view(template_name="index.html"), name='homepage'),

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
