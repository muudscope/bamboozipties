from django.conf.urls.defaults import *


urlpatterns = patterns('blog.views',
    (r'^$', 'apphtml'),

    (r'^list.json$', 'list'),
    (r'^delete/(?P<id>\d+).json$', 'delete'),
    (r'^create.json$', 'create'),
)

