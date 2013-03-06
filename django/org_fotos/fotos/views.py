from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import glob
import os
import shutil

def home(request):
    return render_to_response('fotos/home.html')


def manejador_rutas(request):
    ruta = request.GET['ruta']
    if ruta == '':
        return render_to_response('fotos/home.html', {
            'error_message': "No ingreso la ruta!!!",
            })

    fotos = glob.glob(ruta + '*.jpg')

    if fotos == []:
            return render_to_response('fotos/home.html', {
            'error_message': "No hay ninguna foto en la carpeta especificada",
            })
    request.session['carpeta_acomodar'] = ruta
    return HttpResponseRedirect(reverse('fotos:visor'))

def visor(request):
    if 'carpeta_acomodar' not in request.session:
        return render_to_response('fotos/home.html', {
            'error_message': "Por favor, ingrese la ruta de la carpeta a acomodar",
            })
    fotos = glob.glob(request.session['carpeta_acomodar'] + '*.jpg')
    nombreFoto = os.path.basename(fotos[0])
    return render_to_response('fotos/visor.html', {
        'foto': nombreFoto})

