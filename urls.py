from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'arvtracker.patients.views.index'),
    (r'^upload/$', 'arvtracker.patients.views.upload'),
    (r'^uploader/$', 'arvtracker.patients.views.uploader'),
    (r'^data/$', 'arvtracker.patients.views.data'),
    # Example:
    # (r'^waiting/', include('waiting.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
