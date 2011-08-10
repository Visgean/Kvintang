from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^search/(?P<term>.*)$', "kvintang.dict.views.search"), 
    (r'^$',"kvintang.dict.views.base"),
    (r'^tag/(?P<tag>\d*)$',"kvintang.dict.views.byTag"), 
    (r'^subject/(?P<subject>\d*)$',"kvintang.dict.views.bySubject"), 
    
    (r'^export/$',"kvintang.dict.views.export"), 
    (r'^export/stardict.tab$',"kvintang.dict.views.exportStar"), 
    (r'^export/tag/(?P<tag>\d*)$',"kvintang.dict.views.exportByTag"), 
    (r'^export/subject/(?P<subject>\d*)$',"kvintang.dict.views.exportBySubject"), 
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
