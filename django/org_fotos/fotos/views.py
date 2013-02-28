from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import glob
import os
import shutil

def home(request):
    return render_to_response('fotos/home.html')

def visor(request):
    ruta = request.GET['ruta']
    if ruta == '':
        return render_to_response('fotos/home.html', {
            'error_message': "No ingreso la ruta!!!",
            })

    else:
        fotos = glob.glob(ruta+'*.jpg')

        if fotos == []:
            return render_to_response('fotos/home.html', {
            'error_message': "No hay ninguna foto en la carpeta especificada",
            })

        if not os.path.isdir('temp'):
            os.mkdir('temp')

        shutil.copy(fotos[0], 'temp')
        nombreFoto = os.path.basename(fotos[0])
        context = {'foto': nombreFoto}
        return render(request, 'fotos/visor.html', context)

