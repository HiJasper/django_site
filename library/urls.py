from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('books.views',
    # Examples:
    # url(r'^$', 'library.views.home', name='home'),
    # url(r'^library/', include('library.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^hello/$', 'hello'),
#    url(r'^search_form/$', search_form),
    url(r'search/$', 'search'),
    url(r'contact/$', 'contact'),
)
urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    print "hahhahsdha"
    urlpatterns += patterns('books.views',
        url(r'^display/(\d{1,2})/$', 'display_meta'),
    )
