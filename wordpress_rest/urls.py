from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^v1/', include('wordpress_rest.apps.api.urls', namespace='api')),
)
