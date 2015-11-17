# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 22:06:59 2013

@author: Administrator
"""

from django.conf.urls.defaults import patterns
from newtest.address.models import Address

info_dict = {
#    'model': Address,
    'queryset': Address.objects.all(),
}
urlpatterns = patterns('',
    (r'^/?$', 'django.views.generic.list_detail.object_list', info_dict),
)