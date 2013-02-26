from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def home(request):
    return render_to_response('fotos/home.html')

def visor(request):

    if request.GET['ruta'] == '':
        return render_to_response('fotos/home.html', {
            'error_message': "No ingreso la ruta!!!",
            })

    else:
        return render_to_response('fotos/visor.html')
