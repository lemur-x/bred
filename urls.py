from django.conf.urls.defaults import *
from tableapp.views import main
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
       (r'^$',main),

)
