from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import glob
import os
import shutil


def home(request):
    return render_to_response('home.html')


def manejador_rutas(request):
    ruta = request.GET['ruta']
    if ruta == '':
        return render_to_response(
            'error_rutas.html',
            {'error_message': "No ingreso la ruta!!!"},
        )

    lista_fotos = glob.glob(ruta + '*.jpg')

    if lista_fotos == []:
        return render_to_response(
            'error_rutas.html',
            {'error_message': "No hay ninguna foto en la carpeta especificada",}
        )
    request.session['carpeta_acomodar'] = ruta
    return HttpResponseRedirect(reverse('visor'))


def visor(request):
    lista_fotos = glob.glob(request.session['carpeta_acomodar'] + '*.jpg')
    nombreFoto = os.path.basename(lista_fotos[0])
    context = {
        'foto': nombreFoto,
        'carpeta_actual': request.session['carpeta_acomodar']
    }
    if 'ubicaciones_recientes' in request.session:
        context['ubicaciones'] = request.session['ubicaciones_recientes']

    return render_to_response(
        'visor.html',
        context
    )


def imagen(request, imagen):
    image_data = open(request.session['carpeta_acomodar'] + imagen, "rb").read()
    return HttpResponse(image_data, mimetype="image/jpg")


def acomodador(request):
    pass
