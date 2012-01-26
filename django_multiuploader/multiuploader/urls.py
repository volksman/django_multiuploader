from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^multi/(?P<model_string>\w+\.\w+)/$', 'multiuploader.views.multiuploader', name='multi'),
)
