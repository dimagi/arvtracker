from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^patients/$', 'arvtracker.patients.views.index'),
    (r'^patients/upload/$', 'arvtracker.patients.views.upload'),
    (r'^patients/uploader/$', 'arvtracker.patients.views.uploader'),
    # Example:
    # (r'^waiting/', include('waiting.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
