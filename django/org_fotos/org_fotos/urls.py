from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'fotos.views.home', name='home'),
    url(r'^manejador_rutas/$', 'fotos.views.manejador_rutas'),
    url(r'^visor/$', 'fotos.views.visor', name='visor'),
    url(r'^acomodador/$', 'fotos.views.acomodador'),
    url(r'^imagen/(?P<imagen>[\w\s\.-]+)/$', 'fotos.views.imagen', name='imagen'),
    url(r'^eliminar/(?P<carpeta_id>\d+)/(?P<tipo>\w+)/$', 'fotos.views.eliminar')

    # Examples:
    # url(r'^$', 'org_fotos.views.home', name='home'),
    # url(r'^org_fotos/', include('org_fotos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
