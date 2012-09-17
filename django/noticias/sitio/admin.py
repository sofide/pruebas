from sitio.models import Noticia, Seccion
from django.contrib import admin


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha', 'archivada', 'seccion']

    search_fields = ['titulo', 'texto']

    list_filter = ['fecha', 'archivada', 'seccion']

    date_hierarchy = 'fecha'

class SeccionAdmin(admin.ModelAdmin):
    list_display = ['nombre',]


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Seccion, SeccionAdmin)
