from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from gyf.views import main,book_list
admin.autodiscover()

urlpatterns = patterns('',
#    Examples:
    #url(r'^$', 'gyf1.views.home', name='home'),
#    url(r'^gyf1/', include('gyf1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main),
    url(r'^book_list/$', book_list),
#    url(r'^delete.html/$', Delete),
#    url(r'^search.html/$', Search),
)
