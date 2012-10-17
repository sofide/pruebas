from django.shortcuts import render_to_response
from sitio.models import Noticia, Seccion
from datetime import datetime
import random


def inicio(request):
    nueva = Noticia()
    nueva.titulo = 'entro alguien!'
    nueva.texto = 'acaba de entrar alguien al sitio'
    nueva.fecha = datetime.now()
    nueva.seccion = random.choice(Seccion.objects.all())
    nueva.save()

    noticias = Noticia.objects.all()

    if 'visitas' not in request.session:
        visitas = 0
    else:
        visitas = request.session['visitas']

    request.session['visitas'] = visitas + 1

    return render_to_response('inicio.html', {'lista_noticias': noticias, 'visitas': visitas})


