from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'fotos.view.home'),
    url(r'^visor/$', 'fotos.view.visor'),
    url(r'^acomodador/$', 'fotos.view.acomodador'),

    # Examples:
    # url(r'^$', 'org_fotos.views.home', name='home'),
    # url(r'^org_fotos/', include('org_fotos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)