from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import glob

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
        rFotos = []
        for f in fotos: rFotos.append("'" + f + "'")
        context = {'fotos': rFotos}
        return render(request, 'fotos/visor.html', context)

