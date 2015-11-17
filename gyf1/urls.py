from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from gyf.views import main,searching_result,delete,message,add_author,add_book,edit_book
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
    url(r'^searching_result/$', searching_result),
    url(r'^delete/$', delete),
    url(r'^message/$', message),
    url(r'^add_author/$', add_author),
    url(r'^add_book/$', add_book),
    url(r'^edit_book/$', edit_book),
#    url(r'^delete.html/$', Delete),
#    url(r'^search.html/$', Search),
)
