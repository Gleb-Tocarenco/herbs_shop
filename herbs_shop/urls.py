from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from herbs_shop import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'herbs_shop.views.home', name='home'),
    # url(r'^herbs_shop/', include('herbs_shop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('main_page.urls')), 
    url(r'^admin_page/', include('admin_page.urls')),

)
urlpatterns += patterns('',
	     (r'^static/(?P<path>.*)$', 'django.views.static.serve',         
	    # {'document_root': settings.MEDIA_ROOT}),
	    {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
	)
urlpatterns += patterns('', url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT, }))