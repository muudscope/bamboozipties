from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'homepage.html'}),
    (r'^blog/', include('blog.urls')),

    (r'^admin/', include(admin.site.urls)),

)
