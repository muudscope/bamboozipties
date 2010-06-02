from django.conf.urls.defaults import *


urlpatterns = patterns('blog.views',
    (r'^$', 'apphtml'),

    (r'^list.json$', 'list'),
    (r'^delete/(?P<id>\d+).json$', 'delete'),
    (r'^show/(?P<id>\d+).json$', 'show'),
    (r'^create.json$', 'create'),
    (r'^edit.json$', 'edit'),
)

